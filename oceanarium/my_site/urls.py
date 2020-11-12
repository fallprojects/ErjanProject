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
    path('type_id/<int:pk>/',type_id,name='type_id'),
    path('contacts/',contacts,name='contacts'),
    path('about/',about,name='about'),
    path('entertaimant/<int:pk>/',create_order,name='create_form')

]