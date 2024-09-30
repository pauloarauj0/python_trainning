from django.contrib import admin
from .models import Restaurant, Client, Reservation

admin.site.register(Restaurant)
admin.site.register(Client)
admin.site.register(Reservation)