from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_category


class ProductSeller(models.Model):
    product_Seller = models.CharField(max_length=100)

    def __str__(self):
        return self.product_Seller


class ProductDetail(models.Model):
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_seller = models.ForeignKey(
        ProductSeller, on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField()
    product_available = models.PositiveIntegerField()
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(
        upload_to='uploads/product_images/', blank=True, null=True)

    def __iter__(self):
        return iter(self.__dict__.items())
