from django import forms
from products.models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'brand', 'description', 'price', 'address', 'phone_number', 'tg_username']