


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .models import User, UserType,Address



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "name",
                "class": "form-control"
            }
        ))
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "full name",
                "class": "form-control"
            }
        ))
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    )

    email = forms.EmailField(
        label=_("Email address"),
        help_text=_("Required. Must be a valid email address."),
        required=True,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            "placeholder": "name",
            "class": "form-control"
        })

    )

    mobile = forms.CharField(
        label=_("Mobile number"),
        help_text=_("Optional. Must be in the format '+999999999'. Up to 15 digits allowed."),
        required=False,
        # validators=[mobile_regex],
        widget=forms.TextInput(attrs={
            'autocomplete': 'mobile',
            "placeholder": "pass",
            "class": "form-control"})
    )

    mobile_2 = forms.CharField(
        label=_("Secondary mobile number"),
        help_text=_("Optional. Must be in the format '+999999999'. Up to 15 digits allowed."),
        required=False,
        # validators=[mobile_regex],
        widget=forms.TextInput(attrs={'autocomplete': 'mobile', "placeholder": "name",
            "class": "form-control"})
    )
    password1 = forms.CharField(
        label=_("password"),
        help_text=_("Required. Must be in the format 'capital letter special char number'. Up to 8 digits allowed."),
        required=True,

        widget=forms.PasswordInput(attrs={'autocomplete': 'password', "placeholder": "password",
                                      "class": "form-control"})
    )
    password2 = forms.CharField(
        label=_("Secondary mobile number"),
        help_text=_("Optional. Must be in the format '+999999999'. Up to 15 digits allowed."),
        required=True,

        widget=forms.PasswordInput(attrs={'autocomplete': 'password2', "placeholder": "password2",
                                      "class": "form-control"})
    )

    image = forms.ImageField(
        label=_("Profile image"),
        help_text=_("Required. Must be a valid image file less than 2 MB."),
        required=True,
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*', "placeholder": "name",
            "class": "form-control"})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('email', 'name', 'mobile', 'mobile_2', 'image','password','password2',)
        fields = ('email', 'username','full_name', 'mobile', 'mobile_2', 'image', 'password1', 'password2',)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 2 * 1024 * 1024:
                raise ValidationError(_("Image file size must be less than 2 MB."))
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                raise ValidationError(_("Unsupported file type. Please upload a valid image file."))
        return image


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'mobile', 'mobile_2', 'image',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'mobile', 'mobile_2', 'image')


class UserTypeCreationForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "name",
                "class": "form-control"
            }
        ))
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "full name",
                "class": "form-control"
            }
        ))
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    )

    email = forms.EmailField(
        label=_("Email address"),
        help_text=_("Required. Must be a valid email address."),
        required=True,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            "placeholder": "name",
            "class": "form-control"
        })

    )

    mobile = forms.CharField(
        label=_("Mobile number"),
        help_text=_("Optional. Must be in the format '+999999999'. Up to 15 digits allowed."),
        required=False,
        # validators=[mobile_regex],
        widget=forms.TextInput(attrs={
            'autocomplete': 'mobile',
            "placeholder": "pass",
            "class": "form-control"})
    )

    mobile_2 = forms.CharField(
        label=_("Secondary mobile number"),
        help_text=_("Optional. Must be in the format '+999999999'. Up to 15 digits allowed."),
        required=False,
        # validators=[mobile_regex],
        widget=forms.TextInput(attrs={'autocomplete': 'mobile', "placeholder": "name",
            "class": "form-control"})
    )

    image = forms.ImageField(
        label=_("Profile image"),
        help_text=_("Required. Must be a valid image file less than 2 MB."),
        required=True,
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*', "placeholder": "name",
            "class": "form-control"})
    )
    CHOICES = [
        ('client', 'Client'),
        ('trade', 'Trade'),
        ('supplier', 'Supplier')
    ]
    user_type = forms.CharField(
        widget=forms.Select(
            choices=CHOICES,
            attrs={
                "placeholder": "user_type",
                "class": "form-control"
            }

        ))

    class Meta:
        model = UserType
        fields = ('email', 'username','full_name', 'mobile', 'mobile_2', 'image','user_type')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 2 * 1024 * 1024:
                raise ValidationError(_("Image file size must be less than 2 MB."))
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                raise ValidationError(_("Unsupported file type. Please upload a valid image file."))
        return image


class UserTypeCreationAddressForm(forms.ModelForm):
    postcode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "postcode",
                "class": "form-control"
            }
        ))
    address_line = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "address line",
                "class": "form-control"
            }
        ))

    address_line2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "address line 2",
                "class": "form-control"
            }
        ))

    town_city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "town city ",
                "class": "form-control"
            }
        ))

    delivery_instructions = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "delivery instructions",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Address
        fields = ('postcode', 'address_line', 'address_line2', 'town_city','delivery_instructions')

