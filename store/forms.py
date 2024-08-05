from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models.models import User


class CustomerSignUpForm(UserCreationForm):
    bal = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'bal']


class VendorSignUpForm(UserCreationForm):
    shop_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'shop_name']

