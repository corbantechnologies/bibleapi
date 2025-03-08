from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from versetexts.models import VerseText
from versetexts.serializers import VerseTextSerializer


class VerseTextListCreateView(generics.ListCreateAPIView):
    queryset = VerseText.objects.all()
    serializer_class = VerseTextSerializer
    permission_classes = [
        IsAdminUser,
    ]


class VerseTextRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VerseText.objects.all()
    serializer_class = VerseTextSerializer
    permission_classes = [
        IsAdminUser,
    ]
    lookup_field = "slug"


class VerseTextListView(generics.ListAPIView):
    queryset = VerseText.objects.all()
    serializer_class = VerseTextSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class VerseTextDetailView(generics.RetrieveAPIView):
    queryset = VerseText.objects.all()
    serializer_class = VerseTextSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    lookup_field = "reference"
