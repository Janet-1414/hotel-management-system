from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, RoomCategory


def room_list(request):
    rooms = Room.objects.select_related("category").all()
    return render(request, "rooms/rooms_list.html", {"rooms": rooms})


def room_create(request):
    context = {"form": []}
    return render(request, "rooms/room_form.html", context)


def room_edit(request, pk):
    context = {"form": []}
    return render(request, "rooms/room_form.html", context)


def category_list(request):
    categories = RoomCategory.objects.all()
    return render(request, "rooms/category_list.html", {"categories": categories})


def category_create(request):
    context = {"form": []}
    return render(request, "rooms/category_form.html", context)
