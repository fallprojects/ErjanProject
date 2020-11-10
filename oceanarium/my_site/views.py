from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *

def home_page(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'my_site/home.html',context)

def customer_page(request,pk):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'my_site/customer.html',context)

def entertaimant(request):
    tickets = Ticket.objects.all()
    context = {'tickets':tickets}
    return render(request,'my_site/entertaimant.html',context)

def create_order(request,pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer':customer}
    return render(request, 'my_site/order_form.html',context)


def type(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request,'my_site/type.html', context)

def about(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request, 'my_site/about.html', context)

def contacts(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request, 'my_site/contacts.html', context)

