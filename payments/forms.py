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
            "booking": forms.Select(
                attrs={
                    "class": "block w-full px-3 py-1.5 text-base font-semibold text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-indigo-500"
                }
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "block w-full px-3 py-1.5 text-base font-semibold text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-indigo-500"
                }
            ),
            "payment_type": forms.Select(
                attrs={
                    "class": "block w-full px-3 py-1.5 text-base font-semibold text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-indigo-500"
                }
            ),
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
        elif amount <= 1000:
            raise forms.ValidationError("Amount must be greater than 1000")
        return amount

    def clean_payment_type(self):
        payment_type = self.cleaned_data["payment_type"]
        validy_types = [choice[0] for choice in Payment.PAYMENT_TYPES]
        if payment_type not in validy_types:
            raise forms.ValidationError("Invalid payment type")
        return payment_type
