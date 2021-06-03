from django.shortcuts import render,redirect
from .forms import Createmodelform,ProductCreateform
from .models import Brand,Product
# Create your views here.
def index(request):
    return render(request,'index.html')

def createbrand(request):
    if request.method=="GET":
        form=Createmodelform()
        context={}
        context["form"]=form
        return render(request,'createbrand.html',context)
    elif request.method=="POST":
        form=Createmodelform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html")


def listbrands(request):
    brands= Brand.objects.all()
    context1 = {}
    context1["brands"] = brands
    return render(request, 'listbrand.html', context1)
def delete(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("list")
def update(request,id):
    brand=Brand.objects.get(id=id)
    form=Createmodelform(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=Createmodelform(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request,"update.html",context)

def createproduct(request):
    form=ProductCreateform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreateform(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"createproduct.html",context)
    return render(request,"createproduct.html",context)
def listproduct(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"listproduct.html",context)
def getid(id):
    return Product.objects.get(id=id)
def editproduct(request,*args,**kwargs):
    id=kwargs.get("id")
    product=getid(id)
    form=ProductCreateform(instance=product)
    context={}
    context["form"]=form
    if request.method =="POST":
        form=ProductCreateform(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listproduct")

    return render(request,"editproduct.html",context)
def detailproduct(request,*args,**kwargs):
    id=kwargs.get("id")
    product=getid(id)

    context={}
    context["mobile"]=product
    return render(request,"detailproduct.html",context)
def deleteproduct(request,*args,**kwargs):
    id=kwargs.get("id")
    product=getid(id)
    product.delete()
    return redirect("listproduct")
