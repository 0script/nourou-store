from django.contrib import admin
from .products import Products,Category
from .customer import Customer
from .orders import Order

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)