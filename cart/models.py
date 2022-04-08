from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


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
    product = models.ForeignKey("main.Product",verbose_name=_("Maxsulot"), related_name="pro_orders", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Soni"))
    all_price = models.FloatField(_("Narxi"))

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name+' '+self.user.last_name
        else:
            return self.user.username