from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel,TreeForeignKey
from ..core.models import Extensions

User=get_user_model()

def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "دسته بندی"

    def __str__(self):
        return self.name 


class Product(Extensions):
    seller=models.ForeignKey(User,related_name="user_product",on_delete=models.CASCADE)
    category=TreeForeignKey(Category,related_name="produc_category",on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    views = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.uuid)



    
