from django.db import models
from django.utils.text import slugify

from medicine.models import Product
from users.models import UserType


# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(UserType,on_delete=models.CASCADE,related_name='cart_customer')
    slug = models.SlugField(unique=True)
    product = models.ManyToManyField(Product,related_name='cart_product')
    qty = models.CharField(max_length=50, default=1)
    price = models.CharField(max_length=20,default=0)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.customer)
        self.price = float(self.product.regular_price) * float(self.qty)
        super(Cart, self).save(*args, **kwargs)
