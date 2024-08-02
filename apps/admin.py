from django.contrib import admin

# Register your models here.
from .models import Ticket,Order

admin.site.register(Ticket)
admin.site.register(Order)