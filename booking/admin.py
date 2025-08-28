from django.contrib import admin
from .models import TravelOption, Booking

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'source', 'destination', 'datetime', 'price', 'available_seats')
    list_filter = ('type', 'source', 'destination')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'travel_option', 'number_of_seats', 'total_price', 'status', 'booking_date')
    list_filter = ('status',)
