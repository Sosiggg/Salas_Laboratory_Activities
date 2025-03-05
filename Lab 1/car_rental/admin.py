from django.contrib import admin
from .models import Vehicle, Location, Booking, Review

admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(Review)