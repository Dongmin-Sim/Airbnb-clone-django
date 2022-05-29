from django.urls import path
from rooms import views as room_views

# config urls의 include의 namespace와 동일해야 함.
app_name = 'core'

urlpatterns = [
    path('', room_views.HomeView.as_view(), name="home"),
]