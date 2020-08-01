from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product,Contact,Checkout,Orderupdate,Payment
from math import ceil
import json

def index(request):
    product=Product.objects.all()
    allprods=[]
    cats=Product.objects.values('category','id')
    catall={item['category'] for item in cats}
    for cat in catall:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nslide = n // 4 + ceil(n / 4 - n // 4)
        allprods.append([prod,range(1,nslide),nslide])
    param={'allprods':allprods,'product':product}
    return render(request, 'shop/index2.html', param)
def searchMat(qury,item):
    if qury in item.desc.lower() or qury in item.category.lower() or qury in item.product_name.lower() :
        return True
    else:
        return False

def search(request):
    product = Product.objects.all()
    qury = request.GET.get('search')
    print(qury)
    allprods = []
    cats = Product.objects.values('category', 'id')
    catall = {item['category'] for item in cats}
    for cat in catall:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMat(qury,item)]
        n = len(prod)
        nslide = n // 4 + ceil(n / 4 - n // 4)
        if (len(prod)!=0):
            allprods.append([prod, range(1, nslide), nslide])
    param = {'allprods': allprods, 'product': product,'msg':""}
    if(len(allprods)==0 or len(qury)<4):
        param = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', param)

def about(request):
    products=Product.objects.all()
    params={'product':products,'inno':len(products)}
    return render(request, 'shop/about.html', params)


def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True
        return render(request, 'shop/contact.html',{'thank':thank})
    return render(request, 'shop/contact.html')


def tracker(request):
    Order_id = request.POST.get('order_id', '')
    print(Order_id)
    return render(request, 'shop/tracker.html')


def checkout(request):
    if (request.method=="POST"):
        json_order = request.POST.get('json_order','')
        amount = request.POST.get('amount','')
        first_name=request.POST.get('first_name', '')
        last_name=request.POST.get('last_name', '')
        Address=request.POST.get('Address', '')
        Address_2=request.POST.get('Address_2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip=request.POST.get('zip', '')
        checkout=Checkout(amount=amount, json_order=json_order, first_name=first_name, last_name=last_name, Address=Address, Address_2=Address_2, city=city, state=state, zip=zip)
        checkout.save()
        thank=True
        id=checkout.person_id
        update=Orderupdate(order_id=checkout.person_id,first_name=first_name, updated_desc="Your order has been placed")
        update.save()

        return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')

def payment(request):
    pay=Payment.objects.all()
    return render(request, 'shop/payment.html',{'pay':pay})


def prodview(request,myid):
    #fetch product using id
    product = Product.objects.filter(id=myid)
    param={'product':product}
    return render(request, 'shop/prodview.html',param)

