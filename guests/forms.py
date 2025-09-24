from django import forms
from .models import Guest, Booking


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["first_name", "last_name", "phone_number", "email"]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["guest", "room", "check_in", "check_out"]
