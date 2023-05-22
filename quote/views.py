from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from quote.models import Quote
from quote.utils import get_tmdb_movie

from quote.serializers import QuoteGetSerializer, QuotePostSerializer
# Create your views here.


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuotePostSerializer

    def list(self, request):

        quotes = Quote.objects.all()
        serializer = QuoteGetSerializer(
            quotes, many=True, context={'request': request})

        for quote in serializer.data:
            movie_json = get_tmdb_movie(quote["movie_id"])
            quote.update(movie_json)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        quote = Quote.objects.get(pk=pk)
        serializer = QuoteGetSerializer(quote, context={'request': request})
        movie_json = get_tmdb_movie(serializer.data["movie_id"])
        data = serializer.data.copy()
        data.update(movie_json)
        return Response(data, status=status.HTTP_200_OK)

    @action(url_path='users',detail=True, methods=['get'])
    def quotes_by_user_id(self, request, pk=None):
        quotes = Quote.objects.filter(user=pk)
        return Response("file missing.", status=status.HTTP_404_NOT_FOUND)