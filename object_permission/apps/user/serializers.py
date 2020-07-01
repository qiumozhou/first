#-*-coding:utf-8-*-
from django.contrib.auth.models import Permission, Group
from rest_framework import serializers, permissions

from user.models import User, Token, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude = ['password']
        depth=1


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Token
        exclude=['token_code']
        depth=1

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields="__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"


class GroupPermissionSerializer(serializers.Serializer):
    id=serializers.IntegerField()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        depth=1

class BookoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

