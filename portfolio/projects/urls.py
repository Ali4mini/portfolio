from django.urls import path

from .views import project_detail, projects_list

app_name = "projects"

urlpatterns = [
    path("", projects_list, name="project_list"),
    path("<slug:slug>/", project_detail, name="project_detail"),
]
