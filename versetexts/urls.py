from django.urls import path

from versetexts.views import (
    VerseTextListView,
    VerseTextListCreateView,
    VerseTextDetailView,
    VerseTextRetrieveView,
)

app_name = "versetexts"

urlpatterns = [
    path("", VerseTextListView.as_view(), name="list"),
    path("<str:reference>/", VerseTextDetailView.as_view(), name="detail"),
    path("create/new/", VerseTextListCreateView.as_view(), name="create"),
    path("detail/<str:slug>/", VerseTextRetrieveView.as_view(), name="update"),
]
