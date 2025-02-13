from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Luxury', 'Luxury')])
    transmission = models.CharField(max_length=50, choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')])
    fuel_type = models.CharField(max_length=50, choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    @property
    def rental_days(self):
        return (self.dropoff_date - self.pickup_date).days

    @property
    def total_price(self):
        return self.vehicle.price_per_day * self.rental_days

    def __str__(self):
        return f"{self.user.username} - {self.vehicle.name} - {self.pickup_date} to {self.dropoff_date}"
0
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review {self.id} by {self.user.username}"