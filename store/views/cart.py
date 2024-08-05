from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from store.models.customer import Customer
from store.models.product import Product
from django.views import View
from store.templatetags.cart import price_total


class Cart(View):
    # @login_required
    def get(self, request):
        try:
            ids = list(request.session.get('cart').keys())

            products = Product.get_products_by_id(ids)
            customer_id = request.session.get('customer')
            print(customer_id)
            #customer = Customer.objects.get(id=customer_id)
            customer = self.request.user.customer
            # print(customer)
            cart = request.session.get('cart')
            sum = 0
            for p in products:
                sum += price_total(p, cart)

            if sum <= customer.wallet:
                condition = True

            else:
                condition = False
            return render(request, 'cart.html', {'products' : products, 'customer' : customer, 'checkout':condition})

        except AttributeError:
            return redirect('login')