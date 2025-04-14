from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from datetime import datetime
from products.models import Product, Category, ProductImage
from .forms import NewProductForm
from django.contrib.auth.decorators import login_required


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
        products = Product.objects.all()

        context = {
            'products': products,
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
        products = get_all_products()
        query = request.POST.get('q')
        if query:
            products = Product.objects.filter(title__icontains=query)
        return render(request, 'main/shop.html', {'products':products})
    

    def post(self, request):
        query = request.POST.get('q')
        if query:
            products = Product.objects.filter(title__icontains=query)
            return render(request, 'main/shop.html', {'products':products})
        return redirect("main:shop")
 

class DetailView(View):
    def get(self, request, product_title):
        product = get_object_or_404(Product, title=product_title)
        category = Category.objects.filter(name=product.category.name).first()
        products = Product.objects.filter(category=category)

        product.views += 1
        product.save()

        context = {
            'product': product,
            'products': products,
            }
        
        return render(request, 'main/detail.html', context=context)
    


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
    

@login_required(login_url='login')
def new_product(request):
    if request.method == "GET":
        form = NewProductForm()
        return render(request, 'main/new_product.html', {'form':form})
    elif request.method == "POST":
        form = NewProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(request)
            productimages = []
            for image in request.FILES.getlist("images"):
                productimages.append(ProductImage(image=image, product=product))
            ProductImage.objects.bulk_create(
                productimages
            )
            return redirect('main:index')
        return render(request, 'main/new_product.html', {'form':form})