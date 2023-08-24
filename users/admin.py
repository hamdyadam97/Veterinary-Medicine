from django.contrib import admin

from users.models import User, Address,UserType

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(UserType)