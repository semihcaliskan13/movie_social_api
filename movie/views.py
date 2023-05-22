from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response

from movie.models import Movie
from movie.serializers import MovieSerializer
# Create your views here.


class UserViewSet(viewsets.ViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        
        return super().list(request, *args, **kwargs)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
