from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
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
    # path('detail/<str:product_title>', DetailView.as_view(), name='detail'),
    path('detail/<int:product_id>/', views.DetailView.as_view(), name='detail'), 
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('category/<str:category_name>/', CategoryView.as_view(), name='category')
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)