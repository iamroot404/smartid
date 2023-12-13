from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.models import User
from .models import Account, UserProfile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class UserProfileSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    user = AccountSerializer(many=False)
    class Meta:
        model = UserProfile
        fields = '__all__'
