from django.shortcuts import render
from rest_framework import viewsets
from account.models import MyUser
from account.serializers import UserSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # @action(url_path='quotes',detail=True, methods=['get'])
    # def quotes_by_user_id(self, request, pk=None):
    #     user = MyUser.objects.get(pk=pk)
    #     quotes=user.quote_set.all()#many dataya ulaşabiliyoruz.
    #     serializer = QuotePostSerializer(quotes,context={'request': request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)
