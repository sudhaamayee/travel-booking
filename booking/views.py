from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

from .models import TravelOption, Booking
from .forms import BookingForm

# ---------- Auth ----------
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Username & password are required.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    return render(request, 'booking/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('travel_options')
        messages.error(request, 'Invalid credentials.')
    return render(request, 'booking/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'booking/profile.html')

# ---------- Travel / Booking ----------
def travel_options(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    datetime_str = request.GET.get('date') 
    filter_type = request.GET.get('type') 

    qs = TravelOption.objects.all().order_by('datetime')

    
    if source:
        qs = qs.filter(source__icontains=source)
    if destination:
        qs = qs.filter(destination__icontains=destination)
    if datetime_str:
        qs = qs.filter(datetime__date=datetime_str)
    
    
    if filter_type in {'flight','train','bus'}:
        qs = qs.filter(type=filter_type)

   
    context = {
        'options': qs,
        'source': source,
        'destination': destination,
        'date': datetime_str,
    }
    
    return render(request, 'booking/travel_options.html', context)
    
@login_required
def booking_form(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['number_of_seats']
            if seats > travel.available_seats:
                messages.error(request, 'Not enough seats available.')
            else:
                total = (travel.price or 0) * seats
                booking = Booking.objects.create(
                    user=request.user,
                    travel_option=travel,
                    number_of_seats=seats,
                    total_price=total,
                )
                # reduce seats
                travel.available_seats -= seats
                travel.save()
                return redirect('confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'travel': travel, 'form': form})

def book_travel(request, option_id):
    option = get_object_or_404(TravelOption, id=option_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # assuming user must be logged in
            booking.travel_option = option
            booking.save()
            return redirect('my_bookings')  # redirect to a "my bookings" page
    else:
        form = BookingForm()

    return render(request, 'booking/book_travel.html', {'form': form, 'option': option})

@login_required
def confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking/confirmation.html', {'booking': booking})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('travel_option').order_by('-booking_date')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status != 'cancelled':
        booking.status = 'cancelled'
        booking.save()
        # give seats back
        travel = booking.travel_option
        travel.available_seats += booking.number_of_seats
        travel.save()
        messages.success(request, 'Booking cancelled.')
    return redirect('my_bookings')
