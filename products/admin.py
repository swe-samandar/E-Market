from django.contrib import admin
from .models import Category, Product, ProductImage, Comment



class ProductImageInline(admin.TabularInline):      # bu class Admin panelda Product modelida ProductImage classni Tabular ko'rinishida
    model = ProductImage                            # aks ettirib turadi va bir oynada ikkala class bilan ishlashga yordam beradi


class ProductAdmin(admin.ModelAdmin):                               # Product modelini adminda qanday ko'rinishini boshqaradi
    list_display = ['title', 'id', 'date', 'category',  'author']   # -- namoyish etib turiladigan field lar
    inlines = [ProductImageInline]

admin.site.register(Category)
admin.site.register( Product, ProductAdmin)
admin.site.register( ProductImage)
admin.site.register( Comment)

