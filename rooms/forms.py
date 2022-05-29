from django import forms
from django_countries.fields import CountryField
from . import models

"""
https://docs.djangoproject.com/en/4.0/topics/forms/
Django's rolw in forms 

- preparing and restructuring data to make it ready for rendering
- creating HTML forms for the data
- receiving and processing submitted forms and data from the client
"""

class SearchForm(forms.Form):
    city = forms.CharField(initial='Anywhere')
    country = CountryField(default='KR').formfield()
    room_type = forms.ModelChoiceField(
        queryset=models.RoomType.objects.all(), empty_label="Any kind",
        required=False,
    )
    
    price = forms.IntegerField(required=False, min_value=0)
    guests = forms.IntegerField(required=False, min_value=0)
    bedrooms = forms.IntegerField(required=False, min_value=0)
    beds = forms.IntegerField(required=False, min_value=0)
    bath = forms.IntegerField(required=False, min_value=0)

    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)

    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    

