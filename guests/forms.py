from django import forms
from .models import Guest, Booking


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["first_name", "last_name", "phone_number", "email"]
        error_messages ={
            'first_name':{
                'required':'Please Enter your first name',
                'max_length':'The maximum length should be 100 characters'
            },
            'last_name':{
                'required':'Please Enter your last name',
                'max_length':'The maximum length should be 100 characters'
            },
                'phone_number':{
                'required':'Please Enter your phone number'
            },
            'email':{
                'required':'Please Enter your email address',
                'invalid':'Please enter a valid email'
            }
    
        }
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) <= 2:
            raise forms.ValidationError('Please Enter morethan two characters ')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) <= 2:
            raise forms.ValidationError('Please Enter morethan two characters ')
        return last_name
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 10:
            raise forms.ValidationError('Please Enter a valid phone number')
        return phone_number
    



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["guest", "room", "check_in", "check_out"]
        widgets = {
            'check_in': forms.DateInput(attrs={'type':'date'}),
            'check_out' : forms.DateInput(attrs={'type':'date'}),
        }
        error_messages ={
           
        'guest':{
                'required':'Please Enter guest name'
        },
        'room':{
            'required':'Please Enter a room number'
        },
        'check_in':{
            'required':'Please Enter the check_in date'
        },
        'check_out':{
            'required':'Please Enter the check_out date'
        }

    }

    