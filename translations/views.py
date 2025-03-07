from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

from translations.models import Translation
from translations.serializers import TranslationSerializer

"""
Authenticated
"""
class TranslationsCreateView(generics.CreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [
        IsAdminUser,
    ]


class TranslationRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [
        IsAdminUser,
    ]
    lookup_field = "slug"


"""
Unauthenticated
"""
class TranslationListView(generics.ListAPIView):
    # TODO: Lock this view with consumer keys
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class TranslationDetailView(generics.RetrieveAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    lookup_field = "abbreviation"
