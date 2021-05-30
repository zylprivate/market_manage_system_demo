#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   __init__.py.py

@Time    :   2020/12/31 13:19

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
def init_app(app):
	db.init_app(app)
