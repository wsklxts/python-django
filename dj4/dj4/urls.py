"""dj4 URL Configuration

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
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url,include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
from django.conf.urls import url, include
from rest_framework import routers
from restFramework import views
from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'article', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from rest_framework.authtoken import views as rest_framework_views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^article/$',views.ArticleViewSet.as_view()),
    url(r'^login/$',views.LoginViewSet.as_view()),
    url(r'^snippet/$',views.snippet),
    url(r'^snippet/(?P<pk>\d+)$',views.snippet),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]