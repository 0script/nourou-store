from django.shortcuts import render
from django.core import paginator
from django.core.paginator import Paginator
from .products import Products

# Create your views here.


def home_view(request,*args, **kwargs):

    product_objects = Products.objects.all()
    paginator = Paginator(product_objects,8)
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)

    context={
        'page_title':'Home',
        'product_objects': product_objects,
    }

    #include search functionality
    #get method to the product search view
    # will i use redirect i dont know yet

    return render(request,'product/home.html',context=context)