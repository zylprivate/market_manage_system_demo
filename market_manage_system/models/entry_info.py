#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   entry_info.py

@Time    :   2021/1/3 13:15

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
from .good_info import Goods
class Entry(db.Model):
	ID = db.Column(db.String(255), primary_key=True)
	goods_ID = db.Column(db.String(255), db.ForeignKey('goods.ID'))
	number = db.Column(db.INTEGER)
	time = db.Column(db.DATE)
	state = db.Column(db.SMALLINT)
	total_amount=db.Column(db.INTEGER)
	goods = db.relationship('Goods', backref='entry')
	def __init__(self,ID,goods_ID,number,time,state,total_amount):
		self.ID=ID
		self.goods_ID=goods_ID
		self.number=number
		self.time=time
		self.state=state
		self.total_amount=total_amount
	def __repr__(self):
		return '<entry_ID %r>' % self.ID
	def todict(self):
		return {
			'ID': self.ID,
			'goods_ID': self.goods_ID,
			'number': self.number,
			'time': self.time,
			'state': self.state,
			'total_amount': self.total_amount
		}
