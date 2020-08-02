from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return 'Order {} by {}'.format(self.id, self.user.username)

    class Meta:
        ordering = ('-created',)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='order',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
