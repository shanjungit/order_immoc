# -*- encoding: utf-8 -*-
"""
@File    : www.py
@Time    : 2020/7/22 0:35
@Author  : shanjun.li
@Email   : 739051127@qq.com
@Software: PyCharm
"""
from web.controllers.index import route_index
from application import app

app.register_blueprint(route_index,url_prefix="/")
