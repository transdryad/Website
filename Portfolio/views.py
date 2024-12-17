from django.shortcuts import render
from Projects.models import Project


def portfolio(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "Portfolio/portfolio.html", context)
