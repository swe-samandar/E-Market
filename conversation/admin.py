from django.contrib import admin
from .models import ConversationRoom, Message

# Register your models here.

admin.site.register(Message)
admin.site.register(ConversationRoom)