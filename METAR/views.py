from django.shortcuts import render
from Projects.models import Project


def metar(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "METAR/metar.html", context)
