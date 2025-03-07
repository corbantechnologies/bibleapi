from django.urls import path

from translations.views import (
    TranslationListView,
    TranslationDetailView,
    TranslationsCreateView,
    TranslationRetrieveView,
)

app_name = "translations"

urlpatterns = [
    path("", TranslationListView.as_view(), name="list"),
    path("<str:abbreviation>/", TranslationDetailView.as_view(), name="detail"),
    # Authenticated
    path("create/new/", TranslationsCreateView.as_view(), name="create"),
    path("detail/<str:slug>/", TranslationRetrieveView.as_view(), name="update"),
]
