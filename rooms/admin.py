from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    # admin function
    def used_by(self, obj):
        # obj = queryset - 1row
        return obj.rooms.count()



class PhotoInline(admin.TabularInline):
    model = models.Photo



@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options

    inlines = (
        PhotoInline,
    )

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")}
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "bath")}
        ),
        (
            "More about the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules")
            }
        ),
        (
            "Last Details",
            {"fields": ("host",)}
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
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating"
    )
    
    # ordering = ("name", "price", "bedrooms")

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

    raw_id_fields = (
        "host",
    )

    # admin function
    def count_amenities(self, obj):
        # obj == queryset의 원소 == 1 row
        return obj.amenities.count()

    count_amenities.short_description = "count amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "count photos"
    



@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """
    list_display = ("__str__", 'get_thumbnail',)

    def get_thumbnail(self, obj):
        
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = 'Thumbnail'