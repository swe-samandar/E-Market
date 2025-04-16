from django.urls import path
from .views import (
    IndexView,
    ShopView,
    DetailView,
    ContactView,
    AboutView,
    FAQsView,
    CategoryView,
    new_product,
    product_update,
    product_delete,
)

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/<str:product_title>', DetailView.as_view(), name='detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('category/<str:category_name>/', CategoryView.as_view(), name='category'),
    path('new-product/', new_product, name='new-product'),
    path('update/product/<int:product_id>', product_update, name='update-product'),
    path('delete/product/<int:product_id>/', product_delete, name='delete-product'),
]
