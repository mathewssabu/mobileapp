from django import forms
from .models import Brand,Product


class Createmodelform(forms.ModelForm):
    class Meta():
        model=Brand
        fields=["brand_name"]

class ProductCreateform(forms.ModelForm):
    class Meta():
        model=Product
        fields="__all__"