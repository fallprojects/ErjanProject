from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
