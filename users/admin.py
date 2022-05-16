from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin """
    
    custom_fieldsets = (
        ('Custom Profile', {'fields': ('avatar', 'gender', 'bio', 'birthdate', 'language', 'currency', 'superhost')}),
    )

    fieldsets = custom_fieldsets + UserAdmin.fieldsets
    


    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser"
    ) 

    custom_filter = (
        "superhost",
    )

    list_filter = UserAdmin.list_filter + custom_filter