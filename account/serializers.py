from account.models import MyUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MyUser
        fields = ['url', 'username', 'email', 'is_staff']
        # fields = '__all__'
