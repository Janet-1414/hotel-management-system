from django import forms
from .models import Room, RoomCategory

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'category', 'is_available']
        error_messages = {
            'number':{
                'required':'Please enter the room number',
                'unique': 'This room number is already used',
            },
            'category':{
                'required':'Please enter the room category'
            }
        }


    def clean_number(self):
        number = self.cleaned_data['number']
        if len(number)<2:
            raise forms.ValidationError('please enter more than one character')
        return number


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = "__all__"
        error_messages = {
            'name':{
                'required':'Please enter the category Name',
                'max_length':'Please the maximum should be 100 characters',
            },
            'price_per_night':{
                'required':'Please enter the room price'
                },
        }
    def clean_price_per_night(self):
        price_per_night = self.cleaned_data['price_per_night']
        if price_per_night < 0:
            raise forms.ValidationError('Please enter a price above 0')
        elif price_per_night < 100000:
            raise forms.ValiidationError('please enter price above 10000')
        return price_per_night
    

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Please Enter more than 3 characters')
        if RoomCategory.objects.filter(name=name).exists():
            raise forms.ValidationError('The name already exists')
        return name

