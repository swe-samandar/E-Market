from django.contrib import admin
from .models import Category, Product, ProductImage, Comment

class ProductImageInline(admin.TabularInline):      # bu class Admin panelda Product modelida ProductImage classni Tabular ko'rinishida
    model = ProductImage                            # aks ettirib turadi va bir oynada ikkala class bilan ishlashga yordam beradi


class ProductAdmin(admin.ModelAdmin):                               # Product modelini adminda qanday ko'rinishini boshqaradi
    list_display = ['id', 'title', 'category', 'brand', 'author', 'views']   # -- namoyish etib turiladigan field lar
    inlines = [ProductImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'author', 'body']


admin.site.register(Category, CategoryAdmin)
admin.site.register( Product, ProductAdmin)
admin.site.register( ProductImage)
admin.site.register( Comment, CommentAdmin)

