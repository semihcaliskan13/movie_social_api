from rest_framework import serializers
from quote.models import Quote
from django.contrib.auth.models import User
from account.serializers import UserSerializer


class QuoteGetSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Quote
        fields = '__all__'


class QuotePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['movie_id','movie_name','description','image_path']
