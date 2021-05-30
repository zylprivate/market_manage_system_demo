#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   stock_info.py

@Time    :   2021/1/3 13:14

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from .base import db
from .good_info import Goods
class Stock(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	goods_ID=db.Column(db.String(255),db.ForeignKey('goods.ID'))
	number=db.Column(db.INTEGER)
	plan_time=db.Column(db.DATE)
	state=db.Column(db.SMALLINT)
	goods = db.relationship('Goods', backref='stock')
	def __init__(self,ID,goods_ID,number,plan_time,state):
		self.ID=ID
		self.goods_ID=goods_ID
		self.number=number
		self.plan_time=plan_time
		self.state=state
	def __repr__(self):
		return '<stock_ID %r>' % self.ID
	def todict(self):
		return {
			'ID': self.ID,
			'goods_ID': self.goods_ID,
			'number': self.number,
			'plan_time': self.plan_time,
			'state': self.state
		}
