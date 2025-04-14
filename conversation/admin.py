from django.contrib import admin
from .models import ConversationRoom, Messages

# Register your models here.

admin.site.register(Messages)
admin.site.register(ConversationRoom)