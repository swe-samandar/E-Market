from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    job = models.CharField(max_length=50, blank=True, default='')
    bio = models.CharField(max_length=300, blank=True, default='')
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    class Meta:
        verbose_name = 'customuser'
        verbose_name_plural = 'customusers'
    
    def __str__(self):
        return self.username
    

class SavedProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)