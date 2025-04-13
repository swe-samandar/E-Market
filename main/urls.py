from django.urls import path
from .views import (
    IndexView,
    ShopView,
    DetailView,
    ContactView,
    AboutView,
    FAQsView,
    CategoryView,
)

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('<str:category_name>/category/', CategoryView.as_view(), name='category'),
]