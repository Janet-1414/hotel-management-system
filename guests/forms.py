from django import forms
from .models import Guest, Booking


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["first_name", "last_name", "phone_number", "email"]

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone_number": "Phone Number",
            "email": "Email",
        }

        error_messages = {
            "first_name": {
                "required": "Please Enter the first name",
            },
            "last_name": {"required": "Please Enter the last name"},
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Guest.objects.filter(email=email).exists():
            raise forms.ValidationError("Guest with this email already exists.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if Guest.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Guest with this phone number already exists.")
        return phone_number

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if Guest.objects.filter(first_name=first_name).exists():
            raise forms.ValidationError("Guest with this first name already exists.")
        elif not first_name.isalpha():
            raise forms.ValidationError("First name must be alphabetic")
        elif len(first_name) < 2:
            raise forms.ValidationError("First name must be at least 2 characters")
        else:
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if Guest.objects.filter(last_name=last_name).exists():
            raise forms.ValidationError("Guest with this last name already exists.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must be alphabetic")
        if len(last_name) < 2:
            raise forms.ValidationError("Last name must be at least 2 characters")
        return last_name

    # Use this approach to avoid validating the individual field to check if the indiviudal guest is exiasting in the DB
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name:
            if Guest.objects.filter(
                first_name=first_name, last_name=last_name
            ).exists():
                raise forms.ValidationError(
                    "A guest with this full name already exists."
                )

        return cleaned_data


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

        error_messages = {
            "check_in": {"required": "Check-in date is required"},
            "check_out": {"required": "Check-out date is required"},
        }
