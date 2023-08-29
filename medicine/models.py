
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    class ProductType(models.TextChoices):
        Rivets = "rivets", "Rivets"
        DRINK = "drink", "Drink"
        BAITS = "baits", "Baits"

    product_type = models.CharField(max_length=20, choices=ProductType.choices)
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    last_price = models.DecimalField(
        verbose_name=_("last price"),
        help_text=_("Maximum 9999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 9999.99."),
            },
        },
        max_digits=7,
        decimal_places=2,
        default=0
    )

    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=7,
        decimal_places=2,
    )
    # discount_price = models.DecimalField(
    #     verbose_name=_("Discount price"),
    #     help_text=_("Maximum 9999.99"),
    #     error_messages={
    #         "name": {
    #             "max_length": _("The price must be between 0 and 9999.99."),
    #         },
    #     },
    #     max_digits=7,
    #     decimal_places=2,
    # )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    purchasing_price = models.DecimalField(
        verbose_name=_("purchasing price"),
        help_text=_("Maximum 99999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 9999.99."),
            },
        },
        max_digits=7,
        decimal_places=2,
    )
    # tax_rate = models.DecimalField(
    #     verbose_name=_("tax rate price"),
    #     help_text=_("Maximum 99999.99"),
    #     error_messages={
    #         "name": {
    #             "max_length": _("The price must be between 0 and 9999.99."),
    #         },
    #     },
    #     max_digits=7,
    #     decimal_places=2,
    #     default=0
    # )
    profit = models.DecimalField(
        verbose_name=_("profit price"),
        help_text=_("Maximum 99999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 9999.99."),
            },
        },
        max_digits=7,
        decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    # class Meta:
    #     ordering = ("-created_at",)
    #     verbose_name = _("Product")
    #     verbose_name_plural = _("Products")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.profit = float(self.regular_price) - float(self.purchasing_price)
        super(Product, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("catalogue:product_detail", args=[self.slug])

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
