# -*- coding:utf-8 -*-
# /user/bin/python
from django.forms import Form, fields, widgets
from rbac import models

class LoginForm(Form):

    username = fields.CharField(
        required=True,
        error_messages={"required": "用户名不能为空"},
        widget=widgets.TextInput(attrs={"class": "username", "id": "username", "name":"username", "autocomplete":"off", "placeholder": "请输入用户名"})
    )

    password = fields.CharField(
        required=True,
        error_messages={"required": "密码不能为空"},
        widget=widgets.TextInput(attrs={"type":"password","class": "password", "id": "password", "name":"password", "oncontextmenu":"return false", "onpaste":"return false", "placeholder":"请输入登录密码"})
    )
