# -*- coding:utf-8 -*-
# !/usr/bin/python
class BaseResponse:

    def __init__(self):
        self.status = True
        self.data = None
        self.error = None
        self.msg = None

    def get_dict(self):

        return self.__dict__

class LikeResponse(BaseResponse):

    def __init__(self):
        self.code = 0
        super(LikeResponse, self).__init__()
