from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.orderproduct import OrderProduct
from django.views import View
from store.templatetags.custome_filter import multiply
from store.templatetags.cart import price_total


class CheckOut(View):
    def placeOrder(self):
        self.save()

    # def get(self, request):
    #     customer = request.session.get('customer')
    #     cart = request.session.get('cart')
    #     products = Product.get_products_by_id(list(cart.keys()))
    #     sum = 0
    #     for p in products:
    #         sum += price_total(p, cart)
    #
    #     if sum <= customer.wallet:
    #         condition = True
    #     else:
    #         condition =  False
    #

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = self.request.user.customer
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(customer, address, phone, customer, cart, products)
        # customer = Customer.objects.get(id=customer)
        order = Order(customer=customer, address=address, phone=phone)
        order.save()
        print(len(products))
        for product in products:
            orderproduct = OrderProduct(product=product, price=product.price, quantity=cart.get(str(product.id)),
                                        order=order)
            order.total_price += orderproduct.quantity*product.price
            if(customer.wallet - order.total_price >= 0):
                customer.wallet = customer.wallet - product.price
                customer.save()
                order.save()
            else:
                return redirect(cart)
            # print(product.quantity)
            print(product)
            if (product.quantity - cart.get(str(product.id)) > 0):
                product.quantity = product.quantity - cart.get(str(product.id))
                print(product.quantity)
                orderproduct.save()
                product.save()

        request.session['cart'] = {}
        return redirect('cart')
        # order = Order(customer=Customer(id=customer),orderproduct=OrderProduct(id=orderproduct) )
