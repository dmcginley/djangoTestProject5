from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


CATEGORY = (
    ('S', 'Shirt'),
    ('SP', 'Sport Wear'),
    ('OW', 'Out Wear')
)

LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller')
)


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk": self.pk

        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            "pk": self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            "pk": self.pk
        })
