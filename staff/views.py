from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import staffAuthenticationForm, StaffForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = StaffForm()

    context = {
        "form": form
    }
    return render(request, "staff/registration.html", context)

def login_user(request):
    if request.method == 'POST':
        form = staffAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('room_list')
    else:
        form = staffAuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'staff/login.html', context)

