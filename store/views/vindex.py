from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from django.views import View


class Vproduct(View):
    def get(self, request):
        if self.request.user.is_vendor == True:
            # ids = request.session.get('vendor')
            vendor = self.request.user.vendor

            products = Product.get_all_products_by_vendor(vendor.id)
            print(products)
            return render(request, 'vindex.html', {'products' : products})
        else:
            return redirect('homepage')
