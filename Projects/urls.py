from django.urls import path
from Projects import views

urlpatterns = [
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
