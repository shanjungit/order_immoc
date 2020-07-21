# -*- encoding: utf-8 -*-
"""
@File    : manage.py
@Time    : 2020/7/22 0:32
@Author  : shanjun.li
@Email   : 739051127@qq.com
@Software: PyCharm
"""
from application import app
from application import manager
from flask_script import Server
import www
## web server
manager.add_command("runserver",Server(host="0.0.0.0",port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()