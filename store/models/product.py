from django.db import models
from .category import Category
from .vendor import Vendor


class Product(models.Model):
    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/products/uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)    
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_vendor(vendor_id):
        if vendor_id:
            return Product.objects.filter(vendor=vendor_id)
        # else:
        #     return Product.get_all_products()

