from rest_framework import serializers
from account.serializers import UserSerializer
from quote.models import Quote
from django.contrib.auth.models import User


class QuoteGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Quote
        fields = '__all__'
class QuotePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
