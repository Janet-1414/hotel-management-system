from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm


def payment_list(request):
    payments = Payment.objects.select_related("booking__guest").all()
    return render(request, "payments/payments_list.html", {"payments": payments})


def payment_create(request):
    context = {"form": []}
    return render(request, "payments/payments_form.html", context)
