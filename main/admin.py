from django.contrib import admin
from .models import ProductModel, BasketModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(BasketModel)