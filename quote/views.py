from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


from quote.models import Quote
from quote.permissions import ListMoviesPermission
from quote.utils import get_all_quotes, get_quote
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from quote.serializers import QuoteGetSerializer, QuotePostSerializer
from rest_framework.permissions import *
# Create your views here.


class QuoteViewSet(viewsets.ModelViewSet):
    
    queryset = Quote.objects.all()
    serializer_class = QuotePostSerializer 
    permission_classes = [ListMoviesPermission]
    
    
    
    def list(self, request):
        
        quotes = Quote.objects.all()
        serializer = QuoteGetSerializer(
            quotes, many=True, context={'request': request})

        data = get_all_quotes(serializer.data)

        return Response(data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        quote = Quote.objects.get(pk=pk)
        serializer = QuoteGetSerializer(quote, context={'request': request})
        data = get_quote(serializer.data)
        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    #no user_id in post json, attach the quote with autheticated user in line 43
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = request.user
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(url_path='/deneme', detail=True, methods=['get'])
    def quotes_by_user_id(self, request, pk=None):
        user_quotes = Quote.objects.get(user_id=pk)
        serializer = self.get_serializer(user_quotes)
        data = get_quote(serializer.data)
        return Response(data, status=status.HTTP_200_OK)
# additional route


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_quotes(request, id):

    queryset = Quote.objects.all()
    serializer = QuoteGetSerializer(
    queryset, many=True, context={'request': request})
    data = get_quote(serializer.data)
    return Response(data, status=status.HTTP_200_OK)
