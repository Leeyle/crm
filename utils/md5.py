# -*- coding:utf-8 -*-
# !/usr/bin/python
import hashlib

def md5(pwd):

    obj = hashlib.md5()
    obj.update(pwd.encode('utf-8'))
    data = obj.hexdigest()
    return data
