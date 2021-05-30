#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   supplier_info.py

@Time    :   2021/1/3 13:10

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
class Supplier(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	name = db.Column(db.String(255))
	address = db.Column(db.String(255))
	telephone = db.Column(db.String(255))
	level=db.Column(db.SMALLINT)
	def __init__(self, ID, name, address, telephone,level):
		self.ID = ID
		self.name = name
		self.address = address
		self.telephone = telephone
		self.level=level
	def __repr__(self):
		return '<supplier_name %r>' % self.name
