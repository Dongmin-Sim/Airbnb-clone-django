
from django import http
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render

from django_countries import countries

from . import models


# Create your views here.
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = 'created_at'
    # ~/?page_kwarg=1
    page_kwarg = 'page'

    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['now'] = now
        return context

def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
    
        return render(request=request, template_name='rooms/detail.html', context={'room': room})
    except models.Room.DoesNotExist:
        raise Http404()


def search_view(request):
    print('request get : ',request.GET)

    # search를 위해 클라이언트로부터 받는 정보들
    city = request.GET.get('city', 'Anywhere')
    city = str.capitalize(city)
    country_code = request.GET.get('country', "KR")
    room_type = int(request.GET.get('room_type', 0))
    price = int(request.GET.get('price', 0))
    guests = int(request.GET.get('guests', 0))
    bedrooms = int(request.GET.get('bedrooms', 0))
    beds = int(request.GET.get('beds', 0))
    baths = int(request.GET.get('baths', 0))
    s_amenities = request.GET.getlist('amenities')
    s_facilities = request.GET.getlist('facilities')
    instant_book = bool(request.GET.get('instant_book', False))
    superhost = bool(request.GET.get('superhost', False))

    form = {
        'city': city,
        'country_code': country_code,
        's_room_type': room_type,    
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        'instant_book': instant_book,
        'superhost': superhost,
    }


    # 검색 필터에 들어갈, 서버->클라이언트에 표시될 정보들 
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        'countries': countries,
        'room_types': room_types,
        "amenities": amenities,
        "facilities": facilities,
    }


    # 검색 filter 
    filter_args = {}

    if city != 'Anywhere':
        filter_args['city__startswith'] = city

    filter_args['country'] = country_code

    if room_type != 0:
        filter_args['room_type__pk'] = room_type
        
    if price != 0:
        filter_args['price__lte'] = price

    if guests != 0:
        filter_args['guests__gte'] = guests

    if bedrooms != 0:
        filter_args['bedrooms__gte'] = bedrooms

    if beds != 0:
        filter_args['beds__gte'] = beds

    if baths != 0:
        filter_args['baths__gte'] = baths

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args['amenities__pk'] = int(s_amenity)
    if len(s_amenities) > 0:
        for s_facility in s_facilities:
            filter_args['facilities__pk'] = int(s_facility)

    if instant_book is True:
        filter_args['instant_book'] = True

    if superhost is True:
        filter_args['host__superhost'] = True


    rooms = models.Room.objects.filter(**filter_args)

    context = {
        **form,
        **choices,
        'rooms': rooms,
    }

    return render(request, 'rooms/search.html', context)