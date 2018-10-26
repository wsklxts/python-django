from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ArticleSerializer
from . import models
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# class ArticleViewSet(viewsets.ModelViewSet):
from rest_framework.authentication import  TokenAuthentication ,BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from django.contrib.auth import authenticate, login
from .models import *
def get_random_str(user):
    import hashlib,time
    ctime=str(time.time())

    md5=hashlib.md5(bytes(user,encoding="utf8"))
    md5.update(bytes(ctime,encoding="utf8"))

    return md5.hexdigest()

from django.http import JsonResponse
class LoginViewSet(APIView):
    authentication_classes = []
    permission_classes = ()
    def post(self,request,*args,**kwargs):
        res={"code":1000,"msg":None}
        try:
            user=request._request.POST.get("username")
            pwd=request._request.POST.get("password")
            print(request._request.user)
            print(request._request.user.is_authenticated,33333333333)
            # user_obj=User.objects.filter(username=user,password=pwd).first()
            # user_obj = authenticate(username=user, password=pwd)
            user_obj=userInfo.objects.filter(name=user,pwd=pwd).first()
            print(user_obj,1111111111)
            if not user_obj:
                res["code"]=1001
                res["msg"]="用户名或者密码错误"
            else:
                # UserToken.objects.update_or_create(user=user_obj,defaults={"token":token})
                # token, created = Token.objects.update_or_create(user=user_obj)
                token = get_random_str(user)
                # Token.objects.get_or_create()
                # token = userInfo.objects.update_or_create(id=2,defaults={"name":"bbbbbbbbbbbb"})
                print(token,"t")
                token, c = tokenInfo.objects.update_or_create(user=user_obj,defaults={"key":token})

                # Token.objects.update_or_create(user_id=1, defaults={"key": token})
                # token = Token.objects.filter(user=user_obj).update(key=12313123)
                print(token,c)
                # Token.objects.update_or_create(user=user_obj,defaults={"key":"ssssssssssssssss"})
                res["token"]=token.key

        except Exception as e:
            res["code"]=1002
            res["msg"]=e
        print(res)
        # return JsonResponse(res,json_dumps_params={"ensure_ascii":False})
        return HttpResponse(123)

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # authentication_classes = []
    # authentication_classes = [Authentication,]
    # authentication_classes = (
    #     # BasicAuthentication,
    #     # SessionAuthentication,
    #     # TokenAuthentication,
    # )
    # permission_classes = (
    #     IsAuthenticated,
    # )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        publish_obj = Article.objects.all()
        bs = ArticleSerializer(publish_obj, many=True)
        return Response(bs.data)

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

from .serializers import SnippetSerializer


@api_view(['GET', 'POST', "PUT"])
def snippet(request, *args, **kwargs):
    # snippet1 = models.Snippet.objects.all()
    # Snippets = SnippetSerializer(snippet1, many=True)
    #
    # print(Snippets.data)
    # # return HttpResponse("ok")
    # return Response(Snippets.data)
    id = request.GET.get("id")
    id = kwargs.get("pk") or id

    if request.method == 'GET':

        if not id:
            snippets = models.Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return Response(serializer.data)
        else:
            snippets = models.Snippet.objects.filter(id=id).first()
            serializer = SnippetSerializer(snippets, many=False)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        snippet = models.Snippet.objects.filter(pk=id).first()
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
