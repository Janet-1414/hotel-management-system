from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Staff


class StaffForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['username', 'email','role', 'password1', 'password2']

class staffAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login':"Hello, please check your credentials and try again"
    }