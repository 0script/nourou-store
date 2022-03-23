from django.shortcuts import render
from django.core import paginator
from django.core.paginator import Paginator
from .products import Products

# Create your views here.


def home_view(request,*args, **kwargs):

    queryset= Products.objects.all()
    queryset.order_by('-id')

    #search functionnality
    search_args=request.GET.get('search-input')
    if search_args!='' and search_args is not None:
        #parse text
        search_args.split()
        queryset=queryset.filter(name__icontains=search_args[0])|queryset.filter(category_id__name=search_args[1])|queryset.filter(sexe__icontains=search_args[2])
        queryset=queryset|queryset.filter(name__icontains=search_args[1])|queryset.filter(name__icontains=search_args[2])

    paginator = Paginator(queryset,8)
    page_number=request.GET.get('page')
    queryset=paginator.get_page(page_number)
    
    context={
        'page_title':'Home',
        'product_objects': queryset,
    }

    return render(request,'product/home.html',context=context)
