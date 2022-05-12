from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options

    fieldsets = (
        (
            "Basic Info",
            {"fields": ('name', 'description')}
        ),
    )


    # object outside
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "bath",
        "check_in",
        "check_out",
        "instant_book"
    )
    
    list_filter = (
        'instant_book',
        'host__superhost',
        'room_type',
        'amenities',
        'facilities',
        'house_rules',
        'city',
        'country'
    )


    search_fields = ['=city', '^host__username'] # 외래키로 연결된 field의 항목들도 검색도 가능, foreignkey__field, 정확한 값을 찾으려면 __exact 접미사를 붙이면 됨.
    """
    Useful prefix 
    ^ : startwith
    = : iexact 
    @ : search
    none : icontain
    """

    # object inside
    filter_horizontal = (
        'amenities',
        'facilities',
        'house_rules',
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
