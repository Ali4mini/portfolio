from django.shortcuts import render
from projects.models import Project


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:2]

    context = {"projects": featured_projects}
    return render(request, "home.html", context)
