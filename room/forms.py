from django import forms
from .models import Room, RoomCategory


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ["name", "description", "price_per_night"]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["number", "category", "is_available"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = RoomCategory.objects.all()
