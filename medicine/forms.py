
from django import forms
from django.forms import formset_factory

from .models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_type', 'name', 'regular_price', 'purchasing_price', 'last_price', 'description')


my_form_set = formset_factory(CreateProductForm, extra=12)