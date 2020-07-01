from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
# class UserManager(BaseUserManager): #自定义Manager管理器
#     def _create_user(self,username,password,email,**kwargs):
#         if not username:
#             raise ValueError("请传入用户名！")
#         if not password:
#             raise ValueError("请传入密码！")
#         if not email:
#             raise ValueError("请传入邮箱地址！")
#         user = self.model(username=username,email=email,**kwargs)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_user(self,username,password,email,**kwargs): # 创建普通用户
#         kwargs['is_superuser'] = False
#         return self._create_user(username,password,email,**kwargs)
#
#     def create_superuser(self,username,password,email,**kwargs): # 创建超级用户
#         kwargs['is_superuser'] = True
#         kwargs['is_staff'] = True
#         return self._create_user(username,password,email,**kwargs)


class User(AbstractUser): # 自定义User
    GENDER_TYPE = (
        ("1","男"),
        ("2","女")
    )
    username = models.CharField(max_length=15,unique=True)
    age = models.IntegerField(verbose_name="年龄",null=True)
    gender = models.CharField(max_length=2,choices=GENDER_TYPE,null=True)
    phone = models.CharField(max_length=11,null=True)
    email = models.EmailField()
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # USERNAME_FIELD = 'username' # 使用authenticate验证时使用的验证字段，可以换成其他字段，但验证字段必须是唯一的，即设置了unique=True
    # REQUIRED_FIELDS = ['email'] # 创建用户时必须填写的字段，除了该列表里的字段还包括password字段以及USERNAME_FIELD中的字段
    # EMAIL_FIELD = 'email' # 发送邮件时使用的字段
    # objects = UserManager()

    class Meta:
        db_table = "tb_user"


class Token(models.Model):
    user_id = models.OneToOneField(to='User',on_delete=models.CASCADE)
    token_code = models.CharField(max_length=128)

    class Meta:
        db_table = "tb_token"


class Book(models.Model):
    title=models.CharField(max_length=40)
    date=models.DateTimeField(auto_now_add=True)
    stars=models.IntegerField()
    commiter=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='tb_book'



