from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
from .models import Order
# Create your views here.


def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(name__icontains=item_name)
    
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects':product_objects})

def detail(request,id):
    product_objects = Products.objects.get(id=id)

    return render(request,'shop/detail.html',{'product_objects':product_objects})

def checkout(request):
    if request.method=="POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(total=total,items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode)
        order.save()



    return render(request,'shop/checkout.html')