from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Staff


class StaffForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['username', 'email','role', 'password1', 'password2']
    username = forms.CharField(error_messages={'required':'please enter the user name'})
    email = forms.CharField(error_messages={'required':'please enter your email address'})
    password1 = forms.CharField(error_messages={'required':'please enter your password'})
    password2 = forms.CharField(error_messages={'required':'please enter your password'})
    


class staffAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login':"Hello, please check your credentials and try again"
    }
    username = forms.CharField(error_messages={'required':'please enter the user name'})
    password = forms.CharField(error_messages={'required':'please enter your password'})
