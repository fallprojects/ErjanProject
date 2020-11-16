from django.shortcuts import render,redirect
from django.contrib import messages
from .form import Orderform
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from .form import *


def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization')
    context = {'form':form}
    return render(request,'my_site/registration.html', context)

def authorization(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user is not None:
            return redirect('home')
    context = {}
    return render(request, 'my_site/authorization.html', context)

def logout_page(reguest):
    logout(reguest)
    return redirect('home')


def home_page(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'customers':customers,'orders':orders}
    return render(request,'my_site/home.html',context)

def customer_page(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    context = {'customers':customer,'orders':orders}
    return render(request,'my_site/customer.html',context)

def entertaimant(request):
    tickets = Ticket.objects.all()
    context = {'tickets':tickets}
    return render(request,'my_site/entertaimant.html',context)

def create_order(request,pk):
    ticket = Ticket.objects.get(id=pk)
    customer = request.user.customer
    forms = Orderform(initial={'ticket':ticket},instance=customer)
    if request.method == 'POST':
        forms = Orderform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'forms':forms,'ticket':ticket,'customer':customer}
    return render(request, 'my_site/create_form.html',context)

def type(request):
    types = Type.objects.all()
    context = {'types':types}
    return render(request,'my_site/type.html', context)

def type_id(request,pk):
    type_ids = Type.objects.get(id=pk)
    context = {'type_ids':type_ids}
    return render(request,'my_site/type_id.html',context)

def commit(reguest):
    commits = Commit.objects.all()
    form = Commitform()
    if reguest.method == 'POST':
        form = Commitform(reguest.POST,)
        if form.is_valid():
            form.save()
    context = {'commits':commits,'form':form}
    return render(reguest,'my_site/comments.html', context)

def about(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request,'my_site/about.html', context)

def contacts(request):
    cus = Customer.objects.all()
    context = {'cus':cus}
    return render(request, 'my_site/contacts.html', context)
