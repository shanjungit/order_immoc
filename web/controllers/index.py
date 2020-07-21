# -*- encoding: utf-8 -*-
"""
@File    : index.py
@Time    : 2020/7/22 1:23
@Author  : shanjun.li
@Email   : 739051127@qq.com
@Software: PyCharm
"""
from flask import Blueprint
route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    return "Hello World"
