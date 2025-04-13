from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=150)
    tg_username = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='user_images/', default='user_images/default.png', blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.phone_number}"


class Saved(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE),
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}"
