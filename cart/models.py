from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey("main.Product", related_name="carts", on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField("Soni", default=1)
    price = models.FloatField("Narxi")

    def __str__(self):
        return self.product.name


class MainCart(models.Model):
    carts = models.ManyToManyField(Cart, verbose_name="cart lar")
    all_price = models.FloatField("Jami narxi")

    def __str__(self):
        return self.all_price


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey("main.Product", related_name="pro_orders", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Soni")
    all_price = models.FloatField("Jami narxi")

    def __str__(self):
        return self.user.username