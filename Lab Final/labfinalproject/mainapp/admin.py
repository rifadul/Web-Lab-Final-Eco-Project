from django.contrib import admin
from .models import ProductCategory, ProductDetail, ProductSeller
# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_category']


@admin.register(ProductSeller)
class ProductSellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_Seller']


@admin.register(ProductDetail)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'product_name', 'product_description', 'product_seller',
                    'product_price', 'product_available', 'product_category', 'product_image']
