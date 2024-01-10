from django.urls import path

from .views import order_food

urlpatterns = [
    path('', order_food, name='order_food'),
]