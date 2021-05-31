from django.shortcuts import render,redirect
from .forms import Createmodelform
from .models import Brand
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