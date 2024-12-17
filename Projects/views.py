from django.shortcuts import render
from Projects.models import Project


def project_detail(request, pk):
    projects = Project.objects.all()
    project = Project.objects.get(pk=pk)
    context = {"project": project, "projects": projects}
    return render(request, "Projects/project_detail.html", context)
