"""Файл с классами, отвечающими за отображение моделей в админ-панели Django"""
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentification.models import User
from .forms import UserCreationForm,UserChangeForm, GroupAdminForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    """отображает модель User в админ-панели."""
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'role', 'is_staff')
    list_filter = ('is_staff','role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('role','is_active')}),
        ('Permissions', {'fields': ('is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role','password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class GroupAdmin(admin.ModelAdmin):
    """отображает модель Group в админ-панели."""
    form = GroupAdminForm
    #list_display = [field.name for field in Group._meta.fields]

admin.site.register(User, UserAdmin)
#admin.site.unregister(Group)
#admin.site.register(Group, GroupAdmin)
