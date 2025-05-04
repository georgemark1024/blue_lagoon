from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    reservation_reference = models.CharField(max_length=20, unique=True)
    number_of_rooms = models.PositiveIntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    request_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirmation_time = models.DateTimeField(default=timezone.now)

    customer = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reservation_reference} - {self.customer.first_name} {self.customer.last_name}"

class Hotel(models.Model):
    name = models.CharField(max_length=100, default='Blue Lagoon Hotel and Resort')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=3000)
    total_rooms = models.IntegerField(default=50)
    available_rooms = models.IntegerField(default=50)

    def __str__(self):
        return self.name
