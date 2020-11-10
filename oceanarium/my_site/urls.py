from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('customer/<int:pk>/',customer_page,name='customer'),
    path('entertaimant/',entertaimant,name='entertaimant'),
    path('type/',type,name='type'),
    path('contacts/',contacts,name='contacts'),
    path('about/',about,name='about'),

]