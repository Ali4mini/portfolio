from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _  # Import this
from projects.models import Project

from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]

    # Ensure all strings here are wrapped in _()
    services = [
        {
            "id": "mvp",
            "icon": "fas fa-rocket",
            "title": _("MVP Development"),
            "short": _("From idea to launch."),
            "details": _(
                "I build functional Minimum Viable Products for startups. Includes: Database architecture, User Authentication, payment integration, and deployment."
            ),
            "color": "text-blue-500",
        },
        {
            "id": "api",
            "icon": "fas fa-server",
            "title": _("API & Backend"),
            "short": _("Scalable & Secure."),
            "details": _(
                "High-performance RESTful APIs using Django Rest Framework. Focus on security, JWT authentication, and Redis caching."
            ),
            "color": "text-purple-500",
        },
        {
            "id": "bot",
            "icon": "fas fa-robot",
            "title": _("Automation & Bots"),
            "short": _("Automate the boring stuff."),
            "details": _(
                "Custom Telegram/Discord bots or web scrapers. I help businesses automate repetitive tasks and data collection."
            ),
            "color": "text-green-500",
        },
    ]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect("pages:home")
    else:
        form = ContactForm()

    context = {
        "projects": featured_projects,
        "services": services,
        "form": form,
    }
    return render(request, "home.html", context)
