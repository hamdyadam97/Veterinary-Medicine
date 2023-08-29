
from django import forms
from django.forms import formset_factory

from store.models import Store


class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('product_name', 'new_qty', 'name_company', 'supplier',)


MyFormSet = formset_factory(CreateStoreForm, extra=2)