from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.orderproduct import OrderProduct
from django.views import View
from store.middlewares.auth import auth_middleware
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


class OrderView(LoginRequiredMixin, View):

    def get(self, request):
        customer = self.request.user.customer
        print(customer.id)
        orders = Order.get_orders_by_customer(customer.id)
        #orderproduct = OrderProduct.get_products_by_orderproduct(customer)
        orderproduct = ""
        return render(request, 'orders.html', {'orders' : orders, 'orderproduct' : orderproduct})
