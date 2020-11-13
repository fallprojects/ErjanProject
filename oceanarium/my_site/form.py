from django.forms import ModelForm
from .models import Order, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
