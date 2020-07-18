from django import forms 
from django.forms.widgets import FileInput, TextInput
from .models import Product 

class editProductForm(forms.ModelForm): 
    img = forms.FileField()
    class Meta:
        model = Product 
        fields = ['name', 'img', 'price', 'buy_price', 'quantity']