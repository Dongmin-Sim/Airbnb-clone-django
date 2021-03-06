from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'), 
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('verify/<str:key>', views.complete_verification, name='complete-verification'),
]