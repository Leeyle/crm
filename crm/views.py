from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import View
from django.conf import settings
from utils.response import BaseResponse
from utils.md5 import md5
from rbac.service import init_permission
from rbac.models import *
from crm.forms import *
import re
import json



class Login(View, Form):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form":form})

    def post(self, request, *args, **kwargs):

        msg = BaseResponse()
        form = LoginForm(data=request.POST)
        print(form)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            password = md5(password)
            username = UserInfo.objects.filter(username=username, password=password).first()
            if not username:
                msg.status = False
                msg.error = {}
                msg.error["username"] = "用户名或者密码错误"
                return HttpResponse(json.dumps(msg.__dict__))
            else:
                init_permission.init_permission(request, username)
                return HttpResponse(json.dumps(msg.__dict__))
        else:
            msg.status = False
            msg.error = form.errors
            return HttpResponse(json.dumps(msg.__dict__))


def index(request):

    return render(request, "index.html")



