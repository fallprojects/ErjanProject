from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls import url


urlpatterns = [
    path('',home_page,name='home'),
    path('registration/',registration,name='registration'),
    path('authorization/',authorization,name='authorization'),
    path('logout_page/',logout_page,name='logout_page'),
    path('customer/<int:pk>/',customer_page,name='customer_page'),
    path('entertaimant/',entertaimant,name='entertaimant'),
    path('type/',type,name='type'),
    path('type_id/<int:pk>/',type_id,name='type_id'),
    path('contacts/',contacts,name='contacts'),
    path('about/',about,name='about'),
    path('create_order/<int:pk>/',create_order,name='create_form'),
    path('commit/',commit,name='commit'),
    path('delete/<int:pk>/',delete_order,name='delete')

]

