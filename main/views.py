from django.shortcuts import render
from django.views import View
from datetime import datetime
from products.models import Product
from products.models import Category
from django.shortcuts import get_object_or_404

def for_all_pages(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_today():
    return datetime.date(datetime.today())

# Create your views here.

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        category = Category.objects.all()

        context = {
            'title': 'E-Market',
            'today': get_today(),
            'products': products,
            'category': category,
        }

        return render(request, 'main/index.html', context=context)
    

class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, title=category_name)
        products = Product.objects.filter(category=category)
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'main/category.html', context)


class ShopView(View):
    def get(self, request):

        context = {
            'title': 'E-Market - Product Listing Page',
            'today': get_today()
        }
        
        return render(request, 'main/shop.html', context=context)
    


# class DetailView(View):
#     def get(self, request, product_title):
#         # product = Product.objects.get(title=product_title)
#         product = get_object_or_404(Product, title=product_title)

#         context = {
#             'title': 'E-Market - Product Detail Page',
#             'today': get_today(),
#             'product': product,
#         }
        
#         return render(request, 'main/product_detail.html', context=context)



class DetailView(View):
    def get(self, request, product_id):
        # Now using product_id to get the product
        product = get_object_or_404(Product, id=product_id)

        context = {
            'title': 'E-Market - Product Detail Page',
            'product': product,
        }

        return render(request, 'main/product_detail.html', context)
    


class ContactView(View):
    def get(self, request):

        context = {
            'title': 'E-Market - Contact',
            'today': get_today()
        }
        
        return render(request, 'main/contact.html', context=context)
    


class AboutView(View):
    def get(self, request):

        context = {
            'title': 'E-Market - About Page',
            'today': get_today()
        }
        
        return render(request, 'main/about.html', context=context)



class FAQsView(View):
    def get(self, request):

        context = {
            'title': 'E-Market - FAQs',
            'today': get_today()
        }
        
        return render(request, 'main/faqs.html', context=context)
