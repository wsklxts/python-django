from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
# Create your views here.
from django.middleware.csrf import get_token ,rotate_token

from django.views import View
from .models import userType
from .models import user
from .models import Admin


class Test(View):
    def get(self, request):

        u=user.objects.values()  #单表查询
        t=userType.objects.values().first()
        tl=userType.objects.all()
        a=Admin.objects.get(id=3)
        uu=user.objects.get(id=1)
        return HttpResponse('cbv-get')
    def post(self, request):
        return HttpResponse('cbv-post')

def page(request):
    # for i in range(300):
        # userType.objects.create(name="bbb%s"%(i))

    pageIndex=request.GET.get("pageIndex")
    pageSize=request.GET.get("pageSize")

    start=(int(pageIndex)-1) * int(pageSize)
    end=(int(pageIndex)) * int(pageSize)
    count=  userType.objects.filter(id__lt=111).count()
    olist = userType.objects.filter(id__lt=111).values()[start:end]

    return JsonResponse({"data":list(olist),"pageSum":count},safe=False)

def token(request):
    token = get_token(request)

    return JsonResponse({'token': token})