from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300, blank=False)
    description = models.TextField(blank=True)
    # photo = models.ImageField(upload_to='product_photo',
    #                           blank=True)
    manufacturer = models.CharField(max_length=300,
                                    default='Sri Selvi Sweets')
    price_in_dollars = models.DecimalField(max_digits=6,
                                           decimal_places=2)
