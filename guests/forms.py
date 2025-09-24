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
        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date"}),
            "check_out": forms.DateInput(attrs={"type": "date"}),
        }

        labels = {
            "guest": "Guest",
            "room": "Room",
            "check_in": "Check-in Date",
            "check_out": "Check-out Date",
        }
