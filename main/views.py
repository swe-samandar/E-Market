from django.shortcuts import render
from django.views import View
from datetime import datetime

def get_today():
    return datetime.date(datetime.today())

# Create your views here.

class IndexView(View):
    def get(self, request):

        context = {
            'title': 'E-Market',
            'today': get_today()
        }

        return render(request, 'main/index.html', context=context)
    


class ShopView(View):
    def get(self, request):

        context = {
            'title': 'E-Market - Product Listing Page',
            'today': get_today()
        }
        
        return render(request, 'main/shop.html', context=context)
    


class DetailView(View):
    def get(self, request):

        context = {
            'title': 'E-Market - Product Detail Page',
            'today': get_today()
        }
        
        return render(request, 'main/shop-single.html', context=context)
    


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
