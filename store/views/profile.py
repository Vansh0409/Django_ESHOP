from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from django.views import View
from store.templatetags.cart import price_total


class Profile(View):
    def get(self, request):
        postData = request.POST
        # data = request.POST.get('wallet')
        customer = self.request.user.customer
        # customer.wallet = customer.wallet + int(data)
        return render(request, 'profile.html', {'customer': customer})

    def post(self, request):
        postData = request.POST
        customer = self.request.user.customer
        customer.wallet = customer.wallet + 100
        customer.save()
        return redirect('profile')

