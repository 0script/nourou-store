from django.db import models
from .products import Products
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    price = models.DecimalField(max_digits=15,decimal_places=2)
    address = models.CharField(max_length=50,default='', blank=True)
    phone = models.CharField(max_length=50,blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')