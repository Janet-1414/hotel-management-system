from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'payment_type', 'amount']
        error_messages = {
            'amount':{
                'required':'payment is required',
                'max_length':'The maximum amount should be 100 characters',
                'invalid':'Please Enter a valid number for amount',
            },
            'payment_type':{
                'required':'Please choose a payment method',

            },
            'booking':{
                'required':'Please select a booking of your choice',
            }

        }
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError('Please Enter a positive amount')
        elif amount < 10000:
            raise forms.ValidationError('Please Enter a price above 1000')
        return amount    
