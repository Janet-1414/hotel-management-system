from django import forms
from .models import Room, RoomCategory


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ["name", "description", "price_per_night"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "block w-full px-3 py-2 placeholder-gray-400 text-gray-700"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "block w-full px-3 py-2 placeholder-gray-400 text-gray-700 h-48"
                }
            ),
            "price_per_night": forms.NumberInput(
                attrs={
                    "class": "block w-full px-3 py-2 placeholder-gray-400 text-gray-700"
                }
            ),
        }
        labels = {
            "name": "Name",
            "description": "Description",
            "price_per_night": "Price per Night",
        }
        error_messages = {
            "name": {
                "unique": "Room category already exists",
                "required": "Room category name is required",
            },
            "description": {
                "required": "Room category description is required",
            },
            "price_per_night": {
                "required": "Room category price per night is required",
            },
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 20:
            raise forms.ValidationError(
                "Room category name cannot be more than 20 characters"
            )
        if len(name) < 2:
            raise forms.ValidationError(
                "Room category name cannot be less than 2 characters"
            )
        if RoomCategory.objects.filter(name=name).exists():
            raise forms.ValidationError("Room category name already exists")
        if not name.isalpha():
            raise forms.ValidationError("Room category name must be alphabetic")

        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        if len(description) > 100:
            raise forms.ValidationError(
                "Room category description cannot be more than 100 characters"
            )
        return description

    def clean_price_per_night(self):
        price_per_night = self.cleaned_data["price_per_night"]
        if price_per_night < 0:
            raise forms.ValidationError(
                "Room category price per night cannot be negative"
            )
        return price_per_night


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["number", "category", "is_available"]
        labels = {
            "number": "Room Number",
            "category": "Category",
            "is_available": "Is Available",
        }
        error_messages = {
            "number": {
                "unique": "Room number already exists",
                "required": "Room number is required",
                "max_length": "Room number cannot be more than 10 characters",
                "min_length": "Room number cannot be less than 10 characters",
                "invalid": "Room number is invalid",
            },
            "category": {
                "unique": "Room category already exists",
                "required": "Room category is required",
            },
            "is_available": {
                "required": "Room availability is required",
            },
        }

    def clean_number(self):
        number = self.cleaned_data["number"]
        if Room.objects.filter(number=number).exists():
            raise forms.ValidationError("Room number already exists")
        if len(number) < 2 or len(number) > 4:
            raise forms.ValidationError("Room number must be between 2 and 4 digits")
        return number

    def clean_category(self):
        category = self.cleaned_data["category"]
        if Room.objects.filter(category=category).exists():
            raise forms.ValidationError("Room category already exists")
        return category

    def clean_is_available(self):
        is_available = self.cleaned_data["is_available"]
        if not is_available:
            raise forms.ValidationError("Room is not available")
        return is_available
