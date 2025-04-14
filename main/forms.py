from django import forms
from products.models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'