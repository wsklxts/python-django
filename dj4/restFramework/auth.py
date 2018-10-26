from rest_framework.authentication import  TokenAuthentication ,BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from .models import *

class Authentication(BaseAuthentication):
    def authenticate(self,request):
        token=request._request.GET.get("token")
        token_obj=tokenInfo.objects.filter(key=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("验证失败!")
        return (token_obj.user,token_obj)