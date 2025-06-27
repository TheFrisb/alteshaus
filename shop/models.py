from django.db import models

# Create your models here.
class InternalBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ingredient(InternalBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(InternalBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Product(InternalBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(help_text='Enter a brief description of the product', blank=True)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    ingredients = models.ManyToManyField(Ingredient, related_name='products')

    def __str__(self):
        return self.name

