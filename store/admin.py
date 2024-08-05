from django.contrib import admin
from .models.models import User
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.vendor import Vendor
from .models.reviews import Review
from .models.orders import Order
from .models.orderproduct import OrderProduct

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'vendor']

admin.site.register(User)
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Review)
admin.site.register(OrderProduct)
