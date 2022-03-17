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
    

    custom_display = ('username', 'language', 'currency', 'superhost')
    custom_filter = ('superhost', 'gender', 'language', 'currency', 'superhost')

    list_display = custom_display + UserAdmin.list_display
    list_filter = custom_filter + UserAdmin.list_filter
    
    
