from django.urls import path

from Portfolio import views

urlpatterns = [
    path('', views.portfolio, name='portfolio')
]
