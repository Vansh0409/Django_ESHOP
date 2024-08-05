from django.db import models
from store.models.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)

    @staticmethod
    def get_vendor_by_email(vemail):
        try:
            return Vendor.objects.get(vemail=vemail)
        except:
            return False
    def vregister(self):
        self.save()
    def visExist(self):
        if Vendor.objects.filter(vemail=self.vemail):
            return True
        return False

    @staticmethod
    def get_all_vendors():
        return Vendor.objects.all()