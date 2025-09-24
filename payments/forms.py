from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["booking", "amount", "payment_type"]
        labels = {
            "booking": "Booking",
            "amount": "Amount",
            "payment_type": "Payment Used Type",
        }
        widgets = {
            "booking": forms.Select(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "payment_type": forms.Select(attrs={"class": "form-control"}),
        }
        error_messages = {
            "booking": {
                "required": "Booking is required",
            },
            "amount": {
                "required": "Amount is required",
            },
            "payment_type": {
                "required": "Payment type is required",
            },
        }

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than 0")
        return amount

    def clean_payment_type(self):
        payment_type = self.cleaned_data["payment_type"]
        if payment_type not in Payment.PAYMENT_TYPES:
            raise forms.ValidationError("Invalid payment type")
        return payment_type

    def clean_booking(self):
        booking = self.cleaned_data["booking"]
        if not booking.is_confirmed:
            raise forms.ValidationError("Booking is not confirmed")
        return booking
