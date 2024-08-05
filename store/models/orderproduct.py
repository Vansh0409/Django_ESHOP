from django.db import models
from .product import Product
from .orders import Order
from .customer import Customer
from .vendor import Vendor
import datetime

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()


    @staticmethod
    def get_products_by_orderproduct(order_id):
        return OrderProduct \
            .objects \
            .filter(order=order_id) \
            .order_by('-quantity')


