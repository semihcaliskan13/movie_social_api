from rest_framework import serializers
from movie_social.urls import UserSerializer
from quote.models import Quote
from django.contrib.auth.models import User


class QuoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Quote
        fields = '__all__'
