#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   __init__.py

@Time    :   2020/12/30 9:53

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from flask import Flask
from .  import views
from .  import models
def create_app():
	'''
	instance_relative_config=true  当设置为True时，from_pyfile会从instance_path指定的地址下查找文件
	instsnce_path：不设置，自动寻找与本文件同目录下的instance文件夹
	'''
	app = Flask(__name__, instance_relative_config=True)
	# 寻找instance目录下的文件，此处为config.py
	app.config.from_pyfile('config.py')
	# 添加 jinja 循环控制扩展 使得支持 break 和 continue
	app.jinja_env.add_extension('jinja2.ext.loopcontrols')
	models.init_app(app)
	views.init_app(app)
	return app
