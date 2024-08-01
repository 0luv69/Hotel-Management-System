from multiprocessing.connection import Client
from django.contrib import admin

from accounts.models import Client, Owner
from django.contrib.auth.models import User


admin.site.register(Client)
admin.site.register(Owner)


from .models import User  # Make sure this imports your custom User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_owner', 'is_client')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_owner', 'is_client')}),
    )
    list_display = ('username', 'email', 'is_owner', 'is_client', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
