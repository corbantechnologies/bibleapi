from django.urls import path

from books.views import (
    BookListCreateView,
    BookDetailView,
    BookListView,
    BookRetrieveView,
)

urlpatterns = [
    # unauthenticated
    path("", BookListView.as_view(), name="list"),
    path("<str:reference>/", BookDetailView.as_view(), name="detail"),
    # authenticated
    path("create/new/", BookListCreateView.as_view(), name="create"),
    path("detail/<str:slug>/", BookRetrieveView.as_view(), name="update"),
]
