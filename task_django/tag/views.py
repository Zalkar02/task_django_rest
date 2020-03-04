from rest_framework import generics as g

from .models import Tag
from .serializer import TagSerializer


class TagList(g.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreate(g.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(g.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer