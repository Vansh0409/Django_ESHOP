from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from store.models.customer import Customer
from store.models.vendor import Vendor
from store.forms import CustomerSignUpForm
from store.forms import VendorSignUpForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomerSignUpForm(request.POST)

        if form.is_valid():
            form.instance.is_customer = True
            print(form)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            customer = Customer.objects.create(user=form.instance)
            customer.wallet = request.POST.get('bal')
            customer.save()
            return redirect("homepage")
    form = CustomerSignUpForm()
    return render(request, template_name='reg.html', context={
        'form': form
    })

def vregister(request):
    if request.method == "POST":
        form = VendorSignUpForm(request.POST)

        if form.is_valid():
            form.instance.is_vendor = True
            form.save()
            vendor = Vendor.objects.create(user=form.instance)
            vendor.shop_name = request.POST.get('shop_name')
            vendor.save()
            return redirect("vindex")
    form = VendorSignUpForm()
    return render(request, template_name='reg.html', context={
        'form': form
    })

