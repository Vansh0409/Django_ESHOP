from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.vendor import Vendor
from django.views import View
from django.http import HttpResponseRedirect


class Vlogin(View):
    return_url = None
    def get(self, request):
        Vlogin.return_url=request.GET.get('return_url')
        return render(request, 'vlogin.html')
    def post(self, request):
        email = request.POST.get('vemail')
        password = request.POST.get('vpassword')
        vendor = Vendor.get_vendor_by_email(email)
        error_message = None
        if vendor:
            flag = check_password(password, vendor.vpassword)
            if flag:
                request.session['vendor'] = vendor.id
                if Vlogin.return_url:
                    return HttpResponseRedirect(Vlogin.return_url)
                else:
                    Vlogin.return_url=None
                    return redirect('/vindex')
            else:
                error_message = 'Email or password invalid!'
        else:
            error_message = 'Email or password invalid!'
        return render(request, 'vlogin.html', {'error': error_message})

def vlogout(request):
    request.session.clear()
    return redirect('vlogin')