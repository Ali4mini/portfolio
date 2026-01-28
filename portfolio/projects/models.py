from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = (
        ("web", "Web Development"),
        ("api", "API / Backend"),
        ("bot", "Automation / Bots"),
    )

    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="projects/")
    tools = models.CharField(
        max_length=200, help_text="e.g. Django, Docker, PostgreSQL"
    )

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="web")

    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(
        default=False, help_text="Pin to the top of the Bento Grid"
    )

    # --- English Fields ---
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    description_en = models.TextField(
        help_text="Short summary for the card (English)",
        verbose_name="Summary (English)",
    )
    body_en = models.TextField(
        help_text="Full case study (English)", verbose_name="Body (English)"
    )

    # --- Persian Fields ---
    title_fa = models.CharField(max_length=200, verbose_name="Title (Farsi)")
    description_fa = models.TextField(
        help_text="Short summary for the card (Farsi)", verbose_name="Summary (Farsi)"
    )
    body_fa = models.TextField(
        help_text="Full case study (Farsi)", verbose_name="Body (Farsi)"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title_en  # Return English title by default in Admin

    # Helper to get content based on active language
    def get_title(self):
        from django.utils.translation import get_language

        if get_language() == "fa":
            return self.title_fa
        return self.title_en

    def get_description(self):
        from django.utils.translation import get_language

        if get_language() == "fa":
            return self.description_fa
        return self.description_en

    def get_body(self):
        from django.utils.translation import get_language

        if get_language() == "fa":
            return self.body_fa
        return self.body_en

    def get_tools_list(self):
        """
        Splits 'Django, Docker, Redis' into ['Django', 'Docker', 'Redis']
        """
        if not self.tools:
            return []
        return [tool.strip() for tool in self.tools.split(",")]
