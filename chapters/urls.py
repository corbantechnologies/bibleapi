from django.urls import path

from chapters.views import (
    ChapterListCreateView,
    ChapterRetrieveView,
    ChapterListView,
    ChapterDetailView,
)

app_name = "chapters"

urlpatterns = [
    path("", ChapterListView.as_view(), name="list"),
    path("<str:reference>/", ChapterDetailView.as_view(), name="detail"),
    path("create/new/", ChapterListCreateView.as_view(), name="create"),
    path("detail/<str:slug>/", ChapterRetrieveView.as_view(), name="update"),
]
