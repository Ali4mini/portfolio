from django.shortcuts import get_object_or_404, render

from .models import Project


def project_detail(request, slug):
    # Retrieve project or show 404
    project = get_object_or_404(Project, slug=slug)

    context = {"project": project}
    return render(request, "projects/project_detail.html", context)
