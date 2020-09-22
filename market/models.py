from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(max_length = 500 , verbose_name = 'Description')
    img = models.ImageField(upload_to = 'product_img/' , verbose_name = 'Image')
    created = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.name
    