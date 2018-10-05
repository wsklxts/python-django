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
    csid = request.GET.get("csid")
    result=mysql.change("update ll_student set name=%s,age=%s,csid_id=%s WHERE id=%s", [name,age,csid,id,])
    print(result)
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
    # result = mysql.view("select * from ll_student",[])
    result = mysql.view("select st.id,st.age,st.name,cs.name as csname from ll_student as st left join ll_classes as cs on st.csid_id=cs.id",[])
    callback=request.GET.get("vStudent")
    # allClasses = mysql.view("select * from ll_classes", [])
    http = HttpResponse(callback+"("+json.dumps(result)+")")

    return http

def student(request):

    callback=request.GET.get("callback")
    name=request.GET.get("name")
    age=request.GET.get("age")
    cs=request.GET.get("cs")



    status =mysql.change("insert into ll_student(name,age,csid_id) values(%s,%s,%s)", [name,age,cs])
    result = mysql.view("select id,name,age from ll_student order by id DESC limit 1", [])[0]
    classesId = mysql.view("select * from ll_classes where id=%s", [cs,])[0]
    result["classes"]=classesId
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

    res= mysql.change("delete from ll_classes where id=%s", [uid, ])

    result = {
        "status": res
    }
    print(result)

    return HttpResponse(callback + "(" + json.dumps(result) + ")")

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
    telist = mysql.view("select * from ll_teacher", [])
    relationCs = mysql.view("select cs.id, group_concat(te.id) as teid, cs.name, group_concat(te.name) as telist  from ll_teacher as te  JOIN ll_classes_classestoteacher as cste on te.id=cste.teacher_id  JOIN ll_classes as cs on cs.id=cste.classes_id GROUP BY cs.name", [])
    callback = request.GET.get("getClasees")
    print(relationCs)
    print(result)
    allResult={
        "classes":result,
        "relationCs":relationCs,
        "telist":telist
    }
    return HttpResponse(callback + "(" + json.dumps(allResult) + ")")


def assignTeacher(request):
    callback = request.GET.get("assignTeacher")
    teIds = request.GET.getlist("teId")
    csid = request.GET.get("csid")


    manyVal = []
    for i in teIds:
        manyVal.append((csid,i))

    print(manyVal)
    mysql.change("delete from ll_classes_classestoteacher where classes_id=%s", [csid,])
    result = mysql.manyChange("insert into ll_classes_classestoteacher(classes_id,teacher_id) values(%s,%s)", manyVal)


    return HttpResponse(callback + "(" + json.dumps(result) + ")")
    # return HttpResponse(callback + "('aa')")


def changeTeacher(request):
    callback = request.GET.get("callback")
    name = request.GET.get("name")
    id = request.GET.get("id")

    result=mysql.change("update ll_teacher set name=%s WHERE id=%s", [name,id])

    return HttpResponse(callback + "(" + json.dumps(result) + ")")

def removeTeacher(request):
    uid = request.GET.get("id")
    callback = request.GET.get("callback")

    res=mysql.change("delete from ll_teacher where id=%s",[uid,])

    result={
        "status":res
    }


    return HttpResponse(callback+"("+json.dumps(result)+")")

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