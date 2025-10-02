from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm
from django.contrib.auth.decorators import login_required

@login_required
def payment_list(request):
    if request.user.role != 'MANAGER':
        return redirect('/')
    payments = Payment.objects.select_related("booking__guest").all()
    return render(request, "payments/payments_list.html", {"payments": payments})

@login_required
def payment_create(request):
    if request.user.role != 'MANAGER': 
        return redirect('/')

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    context = {
        "form": form
        }
    return render(request, "payments/payments_form.html", context)
