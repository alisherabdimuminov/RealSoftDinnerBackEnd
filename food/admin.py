from django.contrib import admin

from .models import Food, Order

admin.site.register(Food)
admin.site.register(Order)