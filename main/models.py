from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


class ProductModel(models.Model):
    CATEGORY_CHOICES = [
    ('FANS_AND_CPU_COOLERS', 'Fans & CPU Coolers'),
    ('CASES_CHASSIS', 'Cases / Chassis'),
    ('LAPTOP_NOTEBOOK', 'Laptops / Notebooks'),
]
    STOCK_CHOICES = [
        ('IN_STOCK', 'In stock'),
        ('IN_STOCK_WITH_SUPPLIER', 'In stock with supplier'),
        ('OUT_OF_STOCK', 'Out of stock'),
    ]
    product_name = models.TextField()
    product_description = models.TextField()
    stock_status = models.CharField(max_length=25,choices=STOCK_CHOICES)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    sale_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    image_file = models.CharField(max_length=200)
    component_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0])

    def __str__(self):
        return self.product_name

class BasketModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)