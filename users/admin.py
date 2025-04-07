from django.contrib import admin
from .models import Saved, CustomUser
from django.contrib.auth.models import Group

admin.site.register(CustomUser)
admin.site.register(Saved )
admin.site.unregister(Group)

