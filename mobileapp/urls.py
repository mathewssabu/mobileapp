from django.urls import path
from .views import index,createbrand,listbrands,delete,update
urlpatterns=[
    path('',index),
    path('Brand',createbrand,name="create"),
    path('Brand/create',listbrands,name="list"),
    path('Brand/delete<int:id>',delete,name="delete"),
    path('Brand/<int:id>',update,name="update")
]