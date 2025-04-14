from django.db import models
from users.models import CustomUser

class Messages(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages') # "related_name" bog'langan obyektni ushbu modeldagi obyektlarini olib beradi
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_message')    #   user.sent_messages.all() user jo'natgan barcha xabarlarni beradi
    content = models.TextField()
    status = models.BooleanField(default=False)
    room = models.ForeignKey("ConversationRoom", on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.content}"


class ConversationRoom(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="room_user1")
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="room_user2")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:                                 # Userlar o'rtasida faqat bitta Chat Room ochib beradi, duplicat ChatRoomlarga
        unique_together = ('user1', 'user2')    # yo'l qo'ymaydi


    def __str__(self):
        return f"Chat: {self.user1.username} & {self.user2.username}"

    def participants(self):                     # Chat foydalanuvchilarini ko'rsatib beradi
        return [self.user1, self.user2]         # Chatlashuvchilarni chiqarib beradi

