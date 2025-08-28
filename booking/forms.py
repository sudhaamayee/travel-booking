from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']
        widgets = {
            'number_of_seats': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
