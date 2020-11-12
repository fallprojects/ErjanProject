from django.shortcuts import render,redirect
from django.contrib import messages
from .form import Orderform

from .models import *

def home_page(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'customers':customers,'orders':orders}
    return render(request,'my_site/home.html',context)

def customer_page(request,pk):
    customers = Customer.objects.get(id=pk)
    orders = Customer.order.all()
    context = {'customers':customers,'orders':orders}
    return render(request,'my_site/customer.html',context)

def entertaimant(request):
    tickets = Ticket.objects.all()
    context = {'tickets':tickets}
    return render(request,'my_site/entertaimant.html',context)

def create_order(request,pk):
    ticket = Ticket.objects.get(id=pk)
    forms = Orderform(instance=ticket)
    if request.method == 'POST':
        forms = Orderform(request.POST,instance=ticket)
        if forms.is_valid:
            forms.save()
            return redirect('/')
    context = {'forms':forms,'ticket':ticket}
    return render(request, 'my_site/create_form.html',context)

def type(request):
    types = Type.objects.all()
    context = {'types':types}
    return render(request,'my_site/type.html', context)

def type_id(request,pk):
    type_ids = Type.objects.get(id=pk)
    context = {'type_ids':type_ids}
    return render(request,'my_site/type_id.html',context)

def about(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request, 'my_site/about.html', context)

def contacts(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request, 'my_site/contacts.html', context)

