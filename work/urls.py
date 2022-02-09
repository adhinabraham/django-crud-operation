from django.contrib import admin
from django.urls import URLPattern, path
from . import views


urlpatterns=[
    path('',views.home,),
    path('rooms/<int:pk>',views.rooms, name="rom"),
    path('delete/<int:pk>',views.delete,name="delete"),
]