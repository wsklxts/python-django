from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpRequest,QueryDict,JsonResponse
import django.http
import json
import pymysql
from utils import mysql

# Create your views here.
from ll import models

def hello(request):
    h="aaaaaaaaaaaaaaaaaaaaaaa"
    context = {'h': h,"abs":False}
    context['list']=[1,23,3,4,5,6,6,7]
    print(QueryDict(str(context)))

    return render(request,"hello.html",context)



def changeStudent(request):
    callback = request.GET.get("callback")
    age = request.GET.get("age")
    name = request.GET.get("name")
    id = request.GET.get("id")

    result=mysql.change("update ll_student set name=%s,age=%s WHERE id=%s", [name,age,id])

    return HttpResponse(callback + "(" + json.dumps(result) + ")")

def removeStudent(request):
    uid = request.GET.get("id")
    callback = request.GET.get("callback")

    mysql.change("delete from ll_student where id=%s",[uid,])

    result={
        "status":"成功"
    }


    return HttpResponse(callback+"("+str(result)+")")

def vStudent(request):
    result = mysql.view("select * from ll_student",[])
    callback=request.GET.get("vStudent")
    http = HttpResponse(callback+"("+json.dumps(list(result))+")")
    return http

def student(request):

    callback=request.GET.get("callback")
    name=request.GET.get("name")
    age=request.GET.get("age")

    status =mysql.change("insert into ll_student(name,age) values(%s,%s)", [name,age])
    result = mysql.view("select * from ll_student order by id DESC limit 1", [])[0]
    allresult={
        "status":status,
        "result":result
    }

    return HttpResponse(callback+'( '+json.dumps(allresult)+' )')
    # return HttpResponse(callback+'( "aa" )')



def changeClasses(request):
    callback = request.GET.get("changeClasses")
    name = request.GET.get("name")
    id = request.GET.get("id")

    result = mysql.change("update ll_classes set name=%s WHERE id=%s", [name, id])

    print(name)
    print(id)
    print(request.GET)

    return HttpResponse(callback + "(" + json.dumps(result) + ")")

def removeClasses(request):
    uid = request.GET.get("id")
    callback = request.GET.get("callback")

    mysql.change("delete from ll_classes where id=%s", [uid, ])

    result = {
        "status": "成功"
    }

    return HttpResponse(callback + "(" + str(result) + ")")

def addClasses(request):
    callback = request.GET.get("classes")
    name = request.GET.get("name")

    status = mysql.change("insert into ll_classes(name) values(%s)", [name,])
    result = mysql.view("select * from ll_classes order by id DESC limit 1", [])[0]
    allresult = {
        "status": status,
        "result": result
    }

    return HttpResponse(callback + '( ' + json.dumps(allresult) + ' )')

def getClasees(request):
    result = mysql.view("select * from ll_classes", [])
    callback = request.GET.get("getClasees")

    return HttpResponse(callback + "(" + json.dumps(list(result)) + ")")



def changeTeacher(request):
    callback = request.GET.get("callback")
    name = request.GET.get("name")
    id = request.GET.get("id")

    result=mysql.change("update ll_teacher set name=%s WHERE id=%s", [name,id])

    return HttpResponse(callback + "(" + json.dumps(result) + ")")

def removeTeacher(request):
    uid = request.GET.get("id")
    callback = request.GET.get("callback")

    mysql.change("delete from ll_teacher where id=%s",[uid,])

    result={
        "status":"成功"
    }


    return HttpResponse(callback+"("+str(result)+")")

def getTeacher(request):
    result = mysql.view("select * from ll_teacher",[])
    callback=request.GET.get("getTeacher")

    return HttpResponse(callback+"("+json.dumps(list(result))+")")

def addTeacher(request):

    callback=request.GET.get("callback")
    name=request.GET.get("name")
    status =mysql.change("insert into ll_teacher(name) values(%s)", [name])
    result = mysql.view("select * from ll_teacher order by id DESC limit 1", [])[0]
    allresult={
        "status":status,
        "result":result
    }

    return HttpResponse(callback+'( '+json.dumps(allresult)+' )')
    # return HttpResponse(callback+'( "aa" )')