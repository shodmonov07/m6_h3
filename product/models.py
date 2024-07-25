from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    memory = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    screen = models.CharField(max_length=100, blank=True, null=True)
    processor = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)
    video_card = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
