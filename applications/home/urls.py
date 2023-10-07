# Django Imports
from django.urls import path, include

# Local Imports
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('change-language/<str:new_language>/', views.CambiarIdiomaView.as_view(), name='change-language'),
]