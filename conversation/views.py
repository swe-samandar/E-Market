from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import ConversationRoom, Messages
from .forms import MessageForm
from users.models import CustomUser


def conversation_view(request, room_id):
    room = get_object_or_404(ConversationRoom, id=room_id)
    if request.user not in room.participants():
        return redirect('main:index')

    messages = room.messages.order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = room.user1 if request.user == room.user2 else room.user2
            message.room = room
            message.save()
            return redirect('conversation', room_id=room.id)

    else: form = MessageForm()

    return render(request,'chats/conversation.html', context={'room': room, 'messages': messages, 'form': form})


def start_conversation(request, pk):
    current_user = request.user
    seller = get_object_or_404(CustomUser, pk=pk)

    if current_user==seller:
        return redirect('users:profile', pk)

    user1, user2 = sorted([current_user, seller], key=lambda x: x.pk)

    room, created = ConversationRoom.objects.get_or_create(user1=user1, user2=user2)

    return redirect('conversation', room_id=room.id)


class ConversationListView(View):
    def get(self, request):
        # Conversation room larni chiqaradi
        user = request.user
        notifications = ConversationRoom.objects.filter(user2=user)
        return