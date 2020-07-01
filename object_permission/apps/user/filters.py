#-*-coding:utf-8-*-
import django_filters

from user.models import Token


class userFilter(django_filters.FilterSet):
    token_code = django_filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = Token
        fields = {'token_code'}
