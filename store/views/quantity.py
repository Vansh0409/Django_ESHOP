from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from django.views import View
from store.templatetags.cart import price_total


class Quantity(View):
    def post(self, request, **kwargs):
        postData = request.POST
        product_id = self.kwargs['myid']
        product = Product.objects.get(id=product_id)
        product.quantity = product.quantity + 1
        product.save()
        return redirect('vindex')
