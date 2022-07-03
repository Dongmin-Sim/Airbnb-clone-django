from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_models

# Register your models here.
class RoomInline(admin.TabularInline):
    model = rooms_models.Room



@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin """
    
    inlines = (
        RoomInline,
    )

    custom_fieldsets = (
        ('Custom Profile', {'fields': ('avatar', 'gender', 'bio', 'birthdate', 'language', 'currency', 'superhost', 'email_verified', 'email_secret')}),
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
        "is_superuser",
        "email_verified",
        "email_secret",
    ) 

    custom_filter = (
        "superhost",
    )

    list_filter = UserAdmin.list_filter + custom_filter