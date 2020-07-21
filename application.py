# -*- encoding: utf-8 -*-
"""
@File    : application.py
@Time    : 2020/7/22 0:29
@Author  : shanjun.li
@Email   : 739051127@qq.com
@Software: PyCharm
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
class Application(Flask):
    def __init__(self,import_name):
        super(Application,self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')

        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])
        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__)
print(os.environ.__contains__("ops_config"))
manager = Manager(app)