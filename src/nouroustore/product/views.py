from django.shortcuts import render
from django.core import paginator
from django.core.paginator import Paginator
from .products import Products
from django.db.models import Q 

# Create your views here.


def home_view(request,*args, **kwargs):


    
    product_objects = Products.objects.all()
    product_objects.reverse()
    paginator = Paginator(product_objects,8)

    page_number=request.GET.get('page')
    product_objects=paginator.get_page(page_number)
    
    context={
        'page_title':'Home',
        'product_objects': product_objects,
    }

    #include search functionality
    #get method to the product search view
    # will i use redirect i dont know yet

    return render(request,'product/home.html',context=context)

def seach_product_view(request,*args, **kwargs):
    'get a text from the get request in the url'
    if request.GET.get('search-form'):
 
        try:
            products_obj=Products.objects.filter(name__icontains=)    
    
    return redi()