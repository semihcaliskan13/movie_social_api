from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from quote.models import Quote
from movie.models import Movie
from quote.serializers import QuoteSerializer
# Create your views here.


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
