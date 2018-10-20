from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ("id", "title", "article_type", "content","pub_date") or "__all__"


from .models import Snippet

class SnippetSerializer(ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField()
    # linenos = serializers.BooleanField(required=False)
    # created = serializers.DateTimeField()

    class Meta:
        model = models.Snippet
        fields = "__all__"

    # def create(self, validated_data):
    #     """
    #     根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
    #     """
    #     return Snippet.objects.create(**validated_data)

