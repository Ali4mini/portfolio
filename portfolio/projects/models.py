from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text="A short summary of the project")
    body = models.TextField(
        help_text="Detailed explanation of the problem and your solution"
    )
    image = models.ImageField(upload_to="projects/")
    tools = models.CharField(
        max_length=200, help_text="e.g. Django, Docker, PostgreSQL"
    )
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
