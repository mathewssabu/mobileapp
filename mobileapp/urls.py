from django.urls import path
from .views import index,createbrand,listbrands,delete,update,createproduct,listproduct,editproduct,detailproduct,deleteproduct
urlpatterns=[
    path('',index),
    path('Brand',createbrand,name="create"),
    path('Brand/create',listbrands,name="list"),
    path('Brand/delete<int:id>',delete,name="delete"),
    path('Brand/<int:id>',update,name="update"),
    path("products",createproduct,name="products"),
    path("items",listproduct,name="listproduct"),
    path("items/change <int:id>",editproduct,name="edit"),
    path("items/detail <int:id>",detailproduct,name="view"),
    path("items/remove <int:id>",deleteproduct,name="remove")
]