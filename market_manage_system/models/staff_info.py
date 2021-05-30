#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   staff_info.py

@Time    :   2021/1/2 22:56

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
class  Staff(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	name=db.Column(db.String(255))
	sex=db.Column(db.String(255))
	title=db.Column(db.String(255))
	state=db.Column(db.String(255))
	hire_date=db.Column(db.DATETIME)
	work_age=db.Column(db.INTEGER)
	def __init__(self,ID,name,sex,title,state,hire_date,work_age):
		self.ID=ID
		self.name=name
		self.sex=sex
		self.title=title
		self.state=state
		self.hire_date=hire_date
		self.work_age=work_age
	def __repr__(self):
		return '<staff_name %r>' % self.name
	def todict(self):
		return {
			'ID':self.ID,
			'name':self.name,
			'sex':self.sex,
			'title':self.title,
			'state':self.state,
			'hire_date':self.hire_date,
			'work_age':self.work_age
		}
