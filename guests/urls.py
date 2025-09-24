from django.urls import path
from . import views

urlpatterns = [
    path("", views.guest_list, name="guest_list"),
    path("create/", views.guest_create, name="guest_create"),
    path("booking/create/", views.booking_create, name="booking_create"),
]
