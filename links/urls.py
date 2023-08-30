from django.urls import path

from . import views

# url paths belpow
urlpatterns = [
    path("", views.index, name="home"),
    path("<slug:link_slug>", views.link, name="link-page"),
    path("create/link", views.CreateLinkView.as_view(), name="create-link"),
]
