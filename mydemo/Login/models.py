from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=128)
    class Meta:
        db_table="tb_user"


class UserToken(models.Model):
    user_id=models.OneToOneField(to="Login.User",on_delete=models.CASCADE)
    token=models.CharField(max_length=128)
    class Meta:
        db_table="tb_usertoken"
