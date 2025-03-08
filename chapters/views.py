from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from chapters.models import Chapter
from chapters.serializers import ChapterSerializer


"""
Admin authenticated
"""


class ChapterListCreateView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [
        IsAdminUser,
    ]


class ChapterRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [
        IsAdminUser,
    ]
    lookup_field = "slug"


"""
Unauthenticated
"""


class ChapterListView(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class ChapterDetailView(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    lookup_field = "reference"
