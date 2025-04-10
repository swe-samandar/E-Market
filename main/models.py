from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='productimage_set', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
