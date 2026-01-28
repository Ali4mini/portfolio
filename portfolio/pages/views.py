from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from projects.models import Project

from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Success Message (Bilingual)
            messages.success(
                request,
                _("Your message has been sent successfully! I will contact you soon."),
            )
            # Redirect to home with the #contact anchor so they stay at the form area
            return redirect(request.path + "#contact")
        else:
            messages.error(
                request, _("There was an error in your form. Please check the fields.")
            )
    else:
        form = ContactForm()

    context = {
        "projects": featured_projects,
        "form": form,
    }
    return render(request, "home.html", context)
