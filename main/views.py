from django.shortcuts import render, get_object_or_404
from django.views import View
from datetime import datetime
from products.models import Product, Category

def get_today(request):
    today = datetime.date(datetime.today())
    return {'today': today}

def get_all_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_all_products():
    return Product.objects.all()

# Create your views here.

class IndexView(View):
    def get(self, request):

        context = {}

        return render(request, 'main/index.html', context=context)
    


class ShopView(View):
    def get(self, request):

        context = {
            'products': get_all_products(),
        }
        
        return render(request, 'main/shop.html', context=context)
    


class DetailView(View):
    def get(self, request):
        product = Product.objects.filter().first()
        context = {
            'product': product,
        }
        
        return render(request, 'main/shop-single.html', context=context)
    


class ContactView(View):
    def get(self, request):

        context = {}
        
        return render(request, 'main/contact.html', context=context)
    


class AboutView(View):
    def get(self, request):

        context = {}
        
        return render(request, 'main/about.html', context=context)



class FAQsView(View):
    def get(self, request):

        context = {}
        
        return render(request, 'main/faqs.html', context=context)



class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)

        context = {
            'category': category,
            'products': products,
        }

        return render(request, 'main/category.html', context=context)
    
