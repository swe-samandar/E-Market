from django.db import models
from users.models import CustomUser




class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    


class Product(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    edited_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f"Comment of {self.author.username} for {self.product.title}"
     


    

