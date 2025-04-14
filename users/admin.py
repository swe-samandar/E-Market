from django.contrib import admin

from .models import CustomUser, SavedProduct
from django.contrib.auth.models import Group

# Register your models here.

class SavedProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']   # -- namoyish etib turiladigan field lar

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'phone_number', 'tg_username', 'is_staff']

admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SavedProduct, SavedProductAdmin)

