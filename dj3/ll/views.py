from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from django.forms.models import model_to_dict
from .models import *

def index(request):



    articlelist=Article.objects.all().values()
    # json = serializers.serialize("json",articlelist)
    # print(list(articlelist)[0].get("create_time").strftime("%Y-%m-%d %H:%I:%S"))

    for i in articlelist:
        i["create_time"]=i["create_time"].strftime("%Y-%m:%d %H:%I:%S")
    request.session["user"] = "user"
    return JsonResponse({"data":list(articlelist)},safe=False)
def articleDetail(request):
    id = request.GET.get("id")
    print(dir(request.session))
    articlelist = Article.objects.filter(nid=id).select_related('articledetail').first()
    # articledetail=serializers.serialize('json', )
    # print(type(articlelist.articledetail))
    print(model_to_dict(articlelist.articledetail))
    # articlelist= ArticleDetail.objects.filter(article=id).values()
    # print(articlelist)

    return JsonResponse({"detail": model_to_dict(articlelist.articledetail),"article": model_to_dict(articlelist)}, safe=False)