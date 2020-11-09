from django.shortcuts import render,redirect
from .models import *

def home_page(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'my_site/home.html',context)

