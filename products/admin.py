from django.contrib import admin
from .models import Category, Product, ProductImage, Comment

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'category', 'title', 'date']
    inlines = [ProductImageInline]
    

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Comment)