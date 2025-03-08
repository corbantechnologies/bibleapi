from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from verses.serializers import VerseSerializer
from verses.models import Verse


class VerseListCreateView(generics.ListCreateAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [
        IsAdminUser,
    ]


class VerseRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [
        IsAdminUser,
    ]
    lookup_field = "slug"


class VerseListView(generics.ListAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class VerseDetailView(generics.RetrieveAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    lookup_field = "reference"
