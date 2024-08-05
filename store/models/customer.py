from django.db import models
from store.models.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(default=0)

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username = username)
        except:
            return False
    def register(self):
        self.save()
    def isExist(self):
        if Customer.objects.filter(username=self.username):
            return True
        return False
