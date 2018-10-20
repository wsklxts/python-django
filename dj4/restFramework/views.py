from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . serializers import UserSerializer, GroupSerializer,ArticleSerializer
from . import  models
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer


from .serializers import SnippetSerializer




@api_view(['GET', 'POST'])
def snippet(request):


    # snippet1 = models.Snippet.objects.all()
    # Snippets = SnippetSerializer(snippet1, many=True)
    #
    # print(Snippets.data)
    # # return HttpResponse("ok")
    # return Response(Snippets.data)

    if request.method == 'GET':
        snippets = models.Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)