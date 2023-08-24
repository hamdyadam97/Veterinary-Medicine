from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email, RegexValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


phone_regex = RegexValidator(
    regex=r'^(\+201|01|00201)[0-2,5]{1}[0-9]{8}',
    message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
)


class CustomAccountManager(BaseUserManager):
    def validateEmail(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        if email:
            email = self.normalize_email(email)
            self.validateEmail(email)
        else:
            raise ValueError(_("Superuser Account: You must provide an email address"))

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if email:
            email = self.normalize_email(email)
            self.validateEmail(email)
        else:
            raise ValueError(_("Customer Account: You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=150, )
    full_name = models.CharField(max_length=150,null=True, blank=True)
    mobile = models.CharField(max_length=20, blank=True, validators=[phone_regex])
    mobile_2 = models.CharField(max_length=20, blank=True, validators=[phone_regex])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='users_image', null=True, blank=True,)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "users"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            "l@1.com",
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.username


class UserType(models.Model):
    """
    UserType
    """

    class Type(models.TextChoices):
        CLIENT = "client", "Client"
        TRADE = "trade", "Trade"
        SUPPLIER = "supplier", "Supplier"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True,default='dsa')
    email = models.EmailField(_("email address"), unique=True,null=True)
    username = models.CharField(max_length=150,null=True )
    full_name = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.CharField(max_length=20, blank=True, validators=[phone_regex])
    mobile_2 = models.CharField(max_length=20, blank=True, validators=[phone_regex])
    rate = models.CharField(_("Rate"), max_length=10)
    user_type = models.CharField(max_length=20, choices=Type.choices, default=Type.CLIENT)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    default = models.BooleanField(_("Default"), default=False)
    image = models.ImageField(upload_to='users_type', null=True, blank=True,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(UserType, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "UserType"
        verbose_name_plural = "UserType"

    def __str__(self):
        return "{} Type {}".format(str(self.user_type),str(self.username))


class Address(models.Model):
    """
    Address
    """
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE,null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postcode = models.CharField(_("Postcode"), max_length=50)
    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(_("Address Line 2"), max_length=255)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255,)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    default = models.BooleanField(_("Default"), default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "{} Address".format(self.user_type)