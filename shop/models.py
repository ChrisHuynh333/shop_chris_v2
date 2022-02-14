from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.category}"

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products_in_category")
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Description: {self.description}, Price: {self.price}"

