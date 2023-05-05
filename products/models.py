from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0)
    image = models.ImageField(upload_to='products_images')
    status = models.BooleanField()

    def __str__(self):
        return self.name