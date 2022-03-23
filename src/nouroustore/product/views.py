from django.shortcuts import render
from django.core import paginator
from django.core.paginator import Paginator
from .products import Products,Category
from django.db.models import Q

# Create your views here.


def home_view(request,*args, **kwargs):

    queryset= Products.objects.all()
    queryset.order_by('-id')

    paginator = Paginator(queryset,8)
    page_number=request.GET.get('page')
    queryset=paginator.get_page(page_number)
    
    context={
        'page_title':'Home',
        'product_objects': queryset,
    }

    return render(request,'product/home.html',context=context)

def searchproduct(request):
    if request.method=='GET':
        query=request.GET.get('q')
        
        if query is not None:
            parse_srch=query.split(' ',5)
            print(parse_srch)
            if len(parse_srch)>1:
                parse_srch.pop(-1)
            parse_srch=[i for i in parse_srch if len(i)<10]

            if parse_srch is not []:
                
                #get all brand name and product name in a list 
                name_list=Category.get_all_names()
                brand_list=Category.get_all_brands()
                print(parse_srch)
                q=[]
                for i in parse_srch:
                    print(i)
                    if i in brand_list:
                        q.append(Q(category__brand__icontains=i))
                    if i in name_list:
                        q.append(Q(category__name__icontains=i))
                    q.append(Q(name__icontains=i))
                
                lookups=q[0]
                for i in q:
                    lookups=lookups|i
                
                queryset=Products.objects.filter(lookups).distinct()
                context={
                    'page_title':'Home',
                    'product_objects': queryset,   
                }
                
                paginator = Paginator(queryset,8)
                page_number=request.GET.get('page')
                queryset=paginator.get_page(page_number)
            
                return render(request,'product/home.html',context=context)
