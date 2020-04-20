import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from Login import utils
from Login.models import User, UserToken


class Login(APIView):
    def post(self,request):
        response=dict()
        fields={"username","password"}
        user_info=dict()
        if fields.issubset(set(request.POST.keys())):
            for key in fields:
                user_info[key] = request.data[key]
        user_instance =User.objects.filter(
            username=user_info["username"],
            password = user_info["password"]
        ).first()
        if user_instance:
            access_token=utils.generate_token()
            UserToken.objects.get_or_create(user_id=user_instance,defaults={
                "token":access_token
            })
            response["statu_code"]=200
            response["msg"] = "登录成功"
            response["token"]=access_token
        else:
            response["statu_code"] = 201
            response["msg"] = "登录失败,用户名或密码错误"
        json.dumps(response)
        return JsonResponse(response)
