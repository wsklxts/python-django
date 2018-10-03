"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from ll.views import hello
from ll.views import student
from ll.views import vStudent
from ll.views import removeStudent
from ll.views import changeStudent
from ll.views import addClasses
from ll.views import getClasees
from ll.views import removeClasses
from ll.views import changeClasses
from ll.views import addTeacher
from ll.views import getTeacher
from ll.views import removeTeacher
from ll.views import changeTeacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'student', student),
    path(r'vStudent', vStudent),
    path(r'removeStudent', removeStudent),
    path(r'changeStudent', changeStudent),
    path(r'addClasses', addClasses),
    path(r'getClasees', getClasees),
    path(r'removeClasses', removeClasses),
    path(r'changeClasses', changeClasses),
    path(r'addTeacher', addTeacher),
    path(r'getTeacher', getTeacher),
    path(r'removeTeacher', removeTeacher),
    path(r'changeTeacher', changeTeacher),
    re_path(r".*", hello),
]
