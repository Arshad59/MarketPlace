from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name_plural = "ProductCategories"
        
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory,related_name='product',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(blank=True)
    image = models.ImageField(upload_to='product_images')
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Product, self).delete(*args, **kwargs)
        storage.delete(path)