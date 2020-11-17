from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.full_name

class Ticket(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    Status =(
        ('Sales', 'Sales'),
        ('Sell out', 'Sell out')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    ticket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, choices=Status,default='Sales')

class Type(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    img = models.ImageField(null=True,blank=True)
    text = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

class Commit(models.Model):
    commit = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

class About(models.Model):
    name = models.CharField(max_length=2000, null=True)
    img1 = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=50,null=True)
    img = models.ImageField(null=True, blank=True)
