from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from django_countries import countries

from . import models, forms


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


class SearchView(View):
    def get(self, request):
        print(request.get_full_path())
        if request.GET.get('country'):
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                
                city =  form.cleaned_data.get('city')
                country =  form.cleaned_data.get('country')
                room_type =  form.cleaned_data.get('room_type')
                price =  form.cleaned_data.get('price')
                guests =  form.cleaned_data.get('guests')
                bedrooms =  form.cleaned_data.get('bedrooms')
                beds =  form.cleaned_data.get('beds')
                bath =  form.cleaned_data.get('bath')
                instant_book =  form.cleaned_data.get('instant_book')
                superhost =  form.cleaned_data.get('superhost')
                amenities =  form.cleaned_data.get('amenities')
                facilities =  form.cleaned_data.get('facilities')
                

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if bath is not None:
                    filter_args["bath__gte"] = bath

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                queryset = models.Room.objects.filter(**filter_args)

                for amenity in amenities:
                    # filter_args["amenities"] = amenity
                    queryset = queryset.filter(amenities=amenity)

                for facility in facilities:
                    # filter_args["facilities"] = facility
                    queryset = queryset.filter(facilities=facility)
                
                page = request.GET.get('page', 1)
                queryset = queryset.order_by('-created_at')

                paginator = Paginator(queryset, 3, orphans=1)

                rooms = paginator.get_page(page)

                return render(request, 'rooms/search.html', {'form': form, 'rooms': rooms})

        else:
            form = forms.SearchForm()
        
        # country 값이 있으면서 form 이 not valid 한 경우 
        # country 값이 request에 없는 경우 /rooms/search/
        return render(request, 'rooms/search.html', {'form': form})