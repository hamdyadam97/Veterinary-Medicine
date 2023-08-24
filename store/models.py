from datetime import datetime

from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

from users.models import UserType

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


class Store(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    old_qty = models.CharField(max_length=50, default=0)
    new_qty = models.CharField(max_length=50, default=0)
    total_qty = models.CharField(max_length=20)
    name_company = models.CharField(max_length=20)
    supplier = models.ForeignKey(UserType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        self.total_qty = float(self.old_qty) + float(self.new_qty)
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return ' product of {} name company {} and supplier name is {}'.format(self.product_name, self.name_company,
                                                                               self.supplier)