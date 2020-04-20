#-*-coding:utf-8-*-
from django.conf.urls import url

from Login import views
from Login.views import Login

urlpatterns = [
    url(r'^login/$', Login.as_view(), name="login"),
]
