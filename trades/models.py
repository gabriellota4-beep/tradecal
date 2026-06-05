from django.db import models
from django.contrib.auth.models import User


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.CharField(max_length=50)
    direction = models.CharField(max_length=10)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.instrument} - {self.direction}"