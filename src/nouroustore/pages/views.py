from django.shortcuts import render


# Create your views here.

# Create your views here.
def home_view(request,*args, **kwargs):

    context={
        'page_title':'Home',
    }

    #include search functionality
    #get method to the product search view
    # will i use redirect i dont know yet

    return render(request,'base.html',context=context)