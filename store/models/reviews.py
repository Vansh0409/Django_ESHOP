from django.db import models
from .product import Product
from .customer import Customer
from .vendor import Vendor
import datetime


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=300, default='')

    @staticmethod
    def get_reviews_by_product(product_id):
        return Review.objects.filter(product=product_id)
