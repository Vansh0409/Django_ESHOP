from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        wallet = request.POST.get('wallet')
        value = {'first_name': first_name, 'last_name': last_name, 'phone': phone, 'email': email, 'password': password}

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password, wallet=wallet)
        # Validate
        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name required !!"
        elif customer.first_name:
            if len(customer.first_name) < 4:
                error_message = "First name must be atleast 4 character long."
        if (not customer.last_name):
            error_message = "Last Name required !!"
        elif customer.last_name:
            if len(customer.last_name) < 4:
                error_message = "Last name must be atleast 4 character long."
        if not customer.phone:
            error_message = "Phone number required !!"
        elif customer.phone:
            if len(customer.phone) < 10:
                error_message = "phone number must be 10 digits long."
        isExist = customer.isExist()
        if isExist:
            error_message = "Email Address already registered"
        return error_message

