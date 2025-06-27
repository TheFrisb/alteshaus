from django.contrib import admin

from shop.models import Product, Category, Ingredient


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'regular_price')
    search_fields = ('name',)
    filter_horizontal = ('ingredients',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_products')
    search_fields = ('name',)

    def total_products(self, obj):
        return Product.objects.filter(category=obj).count()

    total_products.short_description = 'Total Products'
    total_products.admin_order_field = 'total_products'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
