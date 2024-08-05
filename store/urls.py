from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, login, signup, vsignup, vindex
from .views.login import Login, logout
from .views.vlogin import Vlogin, vlogout
from .views.profile import Profile
from .views.home import Index, product
from .views.quantity import Quantity
from .views.cart import Cart
from .views.product import UplaodProduct
from .views.vindex import Vproduct
from .views.checkout import CheckOut
from .views.review import RReview
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from .views.views import register
from .views.views import vregister
from django.urls import reverse_lazy

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('vsignup', vsignup.Vsignup.as_view(), name='vsignup'),
    path('vindex', vindex.Vproduct.as_view(), name='vindex'),
    # path('login', Login.as_view(), name='login'),
    path('register', register, name='reg'),
    path('login', auth_views.LoginView.as_view(template_name='log.html'), name='login'),
    path('vlogin', auth_views.LoginView.as_view(template_name='log.html', next_page=reverse_lazy('vindex')), name='vlogin'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('vregister', vregister, name='vreg'),
    path('vlogin', Vlogin.as_view(), name='vlogin'),
    path('vlogout', vlogout, name='vlogout'),
    path('product', UplaodProduct.as_view(), name='product'),
    # path('review', RReview.as_view(), name='review'),
    path('products/<int:myid>', product, name='product'),
    path('vindex/<int:myid>', Quantity.as_view(), name='quantity'),
    path('products/<int:myid>/review', RReview.as_view(), name='review'),
    # path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('profile', Profile.as_view(), name='profile'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
]
