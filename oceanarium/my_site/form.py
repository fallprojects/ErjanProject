from django.forms import ModelForm
from .models import Order, Customer
from django.contrib.auth.models import User
from .models import Commit

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','status']


class Commitform(ModelForm):
    class Meta:
        model = Commit
        fields = '__all__'
