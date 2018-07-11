from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.

def hello(request):
    h="aaaaaaaaaaaaaaaaaaaaaaa"
    context = {'h': h,"abs":False}
    context['list']=[1,23,3,4,5,6,6,7]
    return render(request,"hello.html",context)

def hello1(request):
    return HttpResponse("hello1")