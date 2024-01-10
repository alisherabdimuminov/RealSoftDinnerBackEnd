from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=0, max_digits=10)

    def __str__(self):
        return self.name

class Order(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name
