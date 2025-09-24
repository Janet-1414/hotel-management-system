from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest, Booking
from .forms import GuestForm, BookingForm


def guest_list(request):
    guests = Guest.objects.all()
    return render(request, "guests/guests_list.html", {"guests": guests})


def guest_create(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("guest_list")
    else:
        form = GuestForm()
    return render(request, "guests/guest_form.html", {"form": form})


def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # Mark room as unavailable
            booking.room.is_available = False
            booking.room.save()
            return redirect("guest_list")
    else:
        form = BookingForm()
    return render(request, "guests/booking_form.html", {"form": form})


def guest_edit(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect("guest_list")
    else:
        form = GuestForm(instance=guest)
    return render(request, "guests/guest_form.html", {"form": form})


def guest_delete(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    guest.delete()
    return redirect("guest_list")
