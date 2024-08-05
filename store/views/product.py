from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.category import Category
from store.models.product import Product
from store.models.orders import Order
from store.models.vendor import Vendor
from store.models.reviews import Review
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class UplaodProduct(View):

    def post(self, request):


        postData = request.POST
        name = request.POST.get('name')
        print(self.request.user)
        vendor = self.request.user.vendor

        # vendor = Vendor.objects.filter(id=request.session.get('vendor'))[0]
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = Category.objects.create(name=request.POST.get('category'))
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        product = Product(name=name, vendor=vendor, price=price, quantity=quantity, category=category, desc=desc, image=image)
        product.save()
        data = {
            'name' : name,
            'vendor' : vendor,
            'price' : price,
            'quantity' : quantity,
            'category' : category,
            'desc' : desc,
            'image' : image
        }


        #return render(request, 'vindex.html', data)
        return redirect('vindex')