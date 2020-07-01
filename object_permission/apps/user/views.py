

from django.contrib import auth
from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, Group
from django.utils.decorators import method_decorator
from guardian.decorators import permission_required
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User, Token, Book
from user.serializers import UserSerializer, TokenSerializer, PermissionSerializer, GroupSerializer, \
    GroupPermissionSerializer, BookSerializer, BookoneSerializer
from user.utils import gen_token


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        # 认证token
        token = request.META.get('HTTP_TOKEN')
        if not token:
            raise AuthenticationFailed('尚未认证')
        user_obj = Token.objects.filter(token_code=token)
        if not user_obj:
            raise AuthenticationFailed('非法用户')
        return (user_obj, token)


class UserInfo(APIView):
    authentication_classes = [MyAuth]
    def get(self,request):
        result={}
        token= request.GET.get('token',None)
        if token:
            user=Token.objects.filter(token_code=token).first()
            se=TokenSerializer(user)
            result['data']=se.data
            result['code']=200
            return Response(result)
        else:
            data=User.objects.all().order_by('id')
            page=PageNumberPagination()
            page.page_size = 10
            page.page_query_param = 'page'
            page_list = page.paginate_queryset(data, request)
            ser = UserSerializer(instance=page_list, many=True)
            result['count'] = data.count()
            result['code'] = 200
            result['data'] = ser.data
            return Response(result)

    def post(self,request):
        result={}
        obj={}
        for key in request.data.keys():
            obj[key]=request.data.get(key)
        user=User.objects.create_user(obj['username'],obj['email'],obj['password'])
        user.save()
        user.groups.add(obj['group'])
        result['code']=200
        result['msg']='创建成功'
        return Response(result)

    def delete(self,request):
        result={}
        id=request.data.get('id')
        user=User.objects.get(id=id)
        user.delete()
        result['code']=200
        result['msg']='删除成功'
        return Response(result)

class LoginView(APIView):
    authentication_classes = [] # 使用基础的和token的验证方式
    permission_classes = [] # 允许所有人访问
    def post(self,request):
        result={}
        obj={}
        for key in request.data.keys():
            obj[key] = request.data.get(key)
        user = authenticate(request, username=obj['username'],
                            password=obj['password'])  # 使用authenticate进行登录验证，验证成功会返回一个user对象，失败则返回None
        if user and user.is_active:
            auth.login(request, user)
            token=gen_token()
            Token.objects.update_or_create(user_id=user,defaults={ "token_code":token})
            result['token']=token
            result['code']=200
            result['msg']='验证通过'
            return Response(result)
        elif user and not user.is_active:
            result['code']=201
            result['msg']='用户未激活'
            return Response(result)
        else:
            result['code']=202
            result['msg']='用户名或密码错误！'
            return Response(result)

    def delete(self,request):
        result = {}
        token = request.META.get('HTTP_TOKEN')
        instance=Token.objects.filter(token_code=token).first()
        if instance:
            instance.delete()
            result['code']=200
            result['msg']='退出成功'
            return Response(result)
        else:
            result['code'] = 201
            result['msg'] = '尚未登录'
            return Response(result)



class PermissionView(APIView):
    authentication_classes = [MyAuth]
    def get(self,request):
        result={}
        data=Permission.objects.filter(content_type_id=6)
        se =PermissionSerializer(instance=data,many=True)
        result['data']=se.data
        result['code'] = 200
        return Response(result)


class GroupView(APIView):
    def get(self,request):
        result = {}
        data=Group.objects.all().order_by('id')
        page = PageNumberPagination()
        page.page_size = 10
        page.page_query_param = 'page'
        page_list = page.paginate_queryset(data, request)
        se = GroupSerializer(instance=page_list, many=True)
        result['code']=200
        result['data']=se.data
        result['total']=data.count()
        return Response(result)


    def put(self,request):
        result={}
        name=request.data.get('name')
        obj=Group.objects.filter(name=name).first()
        try:
            obj.permissions.clear()
        except:
            pass
        for id in request.data.get('value'):
            obj.permissions.add(id)
            obj.name=name
        result['code']=200
        result['msg']='修改成功'
        return Response(result)


    def post(self,request):
        result={}
        name=request.data.get('name')
        Group.objects.create(name=name)
        obj=Group.objects.filter(name=name).first()
        for id in request.data.get('value'):
            obj.permissions.add(id)
        result['code']=200
        result['msg']='添加成功'
        return Response(result)

    def delete(self,request):
        result={}
        id=request.data.get('id')
        g=Group.objects.get(id=id)
        g.delete()
        result['code']=200
        result['msg']='删除成功'
        return Response(result)

class GroupPerView(APIView):
    def get(self,request):
        result={}
        id = request.GET.get('id')
        obj = Group.objects.get(id=id)
        datalist = obj.permissions.all()
        se=GroupPermissionSerializer(instance=datalist,many=True)
        result['data']=se.data
        result['code']=200
        return Response(result)

class BookView(APIView):
    @method_decorator(permission_required("user.view_book",raise_exception=True))
    def get(self,request):
        result = {}
        data = Book.objects.all().order_by('id')
        page = PageNumberPagination()
        page.page_size = 10
        page.page_query_param = 'page'
        page_list = page.paginate_queryset(data, request)
        se = BookSerializer(instance=page_list, many=True)
        result['code'] = 200
        result['data'] = se.data
        result['total'] = data.count()
        return Response(result)

    @method_decorator(permission_required("user.add_book", raise_exception=True))
    def post(self,request):
        result={}
        obj={}
        for key in request.data.keys():
            obj[key]=request.data.get(key)
        obj["commiter"]=request.user.id
        se=BookoneSerializer(data=obj)
        se.is_valid()
        se.save()
        result['code']=200
        result['msg']='添加成功'
        return Response(result)

    @method_decorator(permission_required("user.change_book", raise_exception=True))
    def put(self,request):
        result = {}
        obj = {}
        for key in request.data.keys():
            obj[key]=request.data.get(key)
        book=Book.objects.get(id=obj['id'])
        se = BookSerializer(data=obj,instance=book)
        se.is_valid()
        se.save()
        result['code'] = 200
        result['msg'] = '添加成功'
        return Response(result)

    @method_decorator(permission_required("user.delete_book", raise_exception=True))
    def delete(self,request):
        result = {}
        id=request.data.get("id")
        book=Book.objects.get(id=id)
        book.delete()
        result['code'] = 200
        result['msg'] = '删除成功'
        return Response(result)
