from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User, AbstractUser


#

# # Create your models here.
# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password,first_name, last_name, mobile, **extra_fields):
#         if not email:
#             raise ValueError("Email must be provided")
#         if not password :
#             raise ValueError("password must be provided")
#
#         user = self.model(
#             email = self.normalize_email(email),
#             first_name =first_name,
#             last_name =last_name,
#             mobile = mobile,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
#
#     def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, max_length=254)
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     mobile = models.CharField(max_length=50)
#     address = models.CharField(max_length=250)
#
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=True)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
