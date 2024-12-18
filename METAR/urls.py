from django.urls import path
from METAR import views

urlpatterns = [
    path('', views.metar, name='metar')
]
