from django import forms
from .models import Brand


class Createmodelform(forms.ModelForm):
    class Meta():
        model=Brand
        fields=["brand_name"]