from django.db import models

# Create your models here.

class Category(models.Model):
    'Category for product'
    name=models.CharField(max_length=50)
    sexe=models.CharField(max_length=50,default='Mix')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    remise=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=100,default='a short line about the cloth..')
    sexe=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    image_main=models.ImageField(upload_to='media/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_category(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()