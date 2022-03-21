from django.db import models

# Create your models here.

class Customer(models.Model):
    'Model for customer'
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

    def register(self):
        'To save the data'
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    
    @staticmethod
    def get_customer_by_phone(phone):
        try:
            return Customer.objects.get(phone=phone)
        except:
            return False
    
    def isExists(self):
        if Customer.object.filter(email=self.mail):
            return True
        return False

