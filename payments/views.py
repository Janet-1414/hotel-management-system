from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm


def payment_list(request):
    payments = Payment.objects.select_related("booking__guest").all()
    return render(request, "payments/payment_list.html", {"payments": payments})


def payment_create(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payment_list")
    else:
        form = PaymentForm()
    return render(request, "payments/payment_form.html", {"form": form})
