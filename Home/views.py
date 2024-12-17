from django.shortcuts import render
from Projects.models import Project


def home(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "Home/home.html", context)
