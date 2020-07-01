#-*-coding:utf-8-*-
from django.urls import path

from user.views import UserInfo, LoginView, PermissionView, GroupView, GroupPerView, BookView

#
urlpatterns=[
    path(r'user/',UserInfo.as_view()),
    path(r'login/',LoginView.as_view()),
    path(r'permission/', PermissionView.as_view()),
    path(r'group/', GroupView.as_view()),
    path(r'groupper/', GroupPerView.as_view()),
    path(r'book/', BookView.as_view())
]
