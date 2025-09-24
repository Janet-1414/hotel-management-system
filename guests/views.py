from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest, Booking
from .forms import GuestForm, BookingForm


def guest_list(request):
    guests = Guest.objects.all()
    return render(request, "guests/guests_list.html", {"guests": guests})


def guest_create(request):
    context = {"form": []}
    return render(request, "guests/guest_form.html", context)


def booking_create(request):
    context = {"form": []}
    return render(request, "guests/booking_form.html", context)


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "guests/booking_list.html", {"bookings": bookings})


def booking_edit(request, booking_id):
    context = {"form": []}
    return render(request, "guests/booking_form.html", context)


def guest_edit(request, guest_id):
    context = {"form": []}
    return render(request, "guests/guest_form.html", context)


def guest_delete(request, guest_id):
    pass
