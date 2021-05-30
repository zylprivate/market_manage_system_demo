#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   mains.py

@Time    :   2021/1/2 19:38

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from  flask import  Blueprint,render_template
mains_bp=Blueprint('mains',__name__)
@mains_bp.route('/')
def welcome():
	return render_template("welcome.html")
@mains_bp.route('/index')
def index():
	return render_template("index.html")

