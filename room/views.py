from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, RoomCategory
from .forms import RoomForm, RoomCategoryForm


def room_list(request):
    rooms = Room.objects.select_related("category").all()
    return render(request, "rooms/rooms_list.html", {"rooms": rooms})


def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm()
    return render(request, "rooms/room_form.html", {"form": form})


def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(instance=room)
    return render(request, "rooms/room_form.html", {"form": form})
