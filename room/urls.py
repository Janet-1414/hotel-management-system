from django.urls import path
from . import views

urlpatterns = [
    path("", views.room_list, name="room_list"),
    path("create/", views.room_create, name="room_create"),
    path("<int:pk>/edit/", views.room_edit, name="room_edit"),
    # Category paths
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
]
