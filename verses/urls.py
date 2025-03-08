from django.urls import path

from verses.views import (
    VerseListCreateView,
    VerseRetrieveView,
    VerseListView,
    VerseDetailView,
)

app_name = "verses"

urlpatterns = [
    path("", VerseListView.as_view(), name="list"),
    path("<str:reference>/", VerseDetailView.as_view(), name="detail"),
    path("create/new/", VerseListCreateView.as_view(), name="create"),
    path("detail/<str:slug>/", VerseRetrieveView.as_view(), name="update"),
]
