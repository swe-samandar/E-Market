from .views import conversation_view, start_conversation
from django.urls import path

urlpatterns = [
    path('chat/start/<int:pk>/', start_conversation, name='start_conversation'),
    path('conversation/room/<int:room_id>/', conversation_view, name='conversation'),

]