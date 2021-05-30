#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   factory_info.py

@Time    :   2021/1/3 13:10

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
class Factory(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	name=db.Column(db.String(255))
	address=db.Column(db.String(255))
	telephone=db.Column(db.String(255))
	def __init__(self,ID,name,address,telephone):
		self.ID=ID
		self.name=name
		self.address=address
		self.telephone=telephone
	def __repr__(self):
		return '<factory_name %r>' % self.name
	def todict(self):
		return {
			'ID':self.ID,
			'name':self.name,
			'address':self.address,
			'telephone':self.telephone
		}
