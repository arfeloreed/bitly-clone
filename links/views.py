from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.base import View

from .forms import CreateLinkForm
from .models import Link


# Create your views here.
# view route for homepage
def index(request):
    links = Link.objects.all()

    return render(
        request,
        "links/index.html",
        {
            "links": links,
        },
    )


# view route if a link is click
def link(request, link_slug):
    selected_link = get_object_or_404(Link, slug=link_slug)
    # increment the clicks field in the model database everytime a link is click
    selected_link.click()

    return redirect(selected_link.url)


# view route for creating link
class CreateLinkView(View):
    def get(self, request):
        form = CreateLinkForm()
        return render(
            request,
            "links/create-link.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = CreateLinkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("home"))

        return render(
            request,
            "links/create-link.html",
            {
                "form": form,
            },
        )
