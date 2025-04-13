from django.contrib import admin

from .models import CustomUser, SavedProduct
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)
admin.site.register(CustomUser)
admin.site.register(SavedProduct)

