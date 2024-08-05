from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from store.models.vendor import Vendor

class Vsignup(View):
    def get(self, request):
        return render(request, 'vsignup.html')
    def post(self, request):
        postData = request.POST
        name = request.POST.get('name')
        shop_name = request.POST.get('shop_name')
        vphone = request.POST.get('vphone')
        vemail = request.POST.get('vemail')
        vpassword = request.POST.get('vpassword')
        value = {'name': name, 'shop_name': shop_name, 'vphone': vphone, 'vemail': vemail, 'vpassword': vpassword}

        vendor = Vendor(name=name, shop_name=shop_name, vphone=vphone, vemail=vemail, vpassword=vpassword)
        # Validatev
        verror_message = self.validateVendor(vendor)

        if not verror_message:
            vendor.vpassword = make_password(vendor.vpassword)
            vendor.vregister()
            return redirect('vlogin')
        else:
            data = {
                'error': verror_message,
                'values': value
            }
            return render(request, 'vsignup.html', data)

    def validateVendor(self, vendor):
        verror_message = None
        if (not vendor.name):
            verror_message = "Name required !!"
        elif vendor.name:
            if len(vendor.name) < 4:
                verror_message = "Name must be atleast 4 character long."
        if (not vendor.shop_name):
            verror_message = "Shop Name required !!"
        elif vendor.vphone:
            if len(vendor.vphone) < 10:
                verror_message = "phone number must be 10 digits long."
        visExist = vendor.visExist()
        if visExist:
            verror_message = "Email Address already registered"
        return verror_message

