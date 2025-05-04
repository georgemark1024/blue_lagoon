from django.contrib import admin
from . models import Hotel, Reservation, Client

admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Client)

