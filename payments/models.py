from django.db import models
from guests.models import Booking


class Payment(models.Model):
    PAYMENT_TYPES = [
        ("CASH", "Cash"),
        ("CARD", "Card"),
        ("MOBILE", "Mobile Money"),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.guest} - {self.amount} ({self.payment_type})"

    class Meta:
        ordering = ["-date_paid"]
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
