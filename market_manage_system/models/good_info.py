#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   good_info.py

@Time    :   2021/1/2 20:35

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
from .factory_info import Factory
from .supplier_info import Supplier
class Goods(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	name=db.Column(db.String(255))
	price=db.Column(db.String(255))
	bar_code=db.Column(db.String(255))
	inventory=db.Column(db.INTEGER)
	promotion_price=db.Column(db.String(255))
	start_time=db.Column(db.DATETIME)
	end_time=db.Column(db.DATETIME)
	state=db.Column(db.SMALLINT)
	limit_num=db.Column(db.INTEGER)
	factory_ID=db.Column(db.String(255),db.ForeignKey('factory.ID'))
	supplier_ID=db.Column(db.String(255),db.ForeignKey('supplier.ID'))
	factory=db.relationship('Factory',backref='goods')
	supplier=db.relationship('Supplier',backref='goods')
	def __init__(self,ID,name,price,bar_code,inventory=None,promotion_price=None,start_time=None,end_time=None,state=None,limit_num=None,factory_ID=None,supplier_ID=None):
		self.ID=ID
		self.name=name
		self.price=price
		self.bar_code=bar_code
		self.inventory=inventory
		self.promotion_price=promotion_price
		self.start_time=start_time
		self.end_time=end_time
		self.state=state
		self.limit_num=limit_num
		self.factory_ID=factory_ID
		self.supplier_ID=supplier_ID
	def __repr__(self):
		return '<goods_name %r>' % self.name
	def todict(self):
		return {
			'ID':self.ID,
			'name':self.name,
			'price':self.price,
			'bar_code':self.bar_code,
			'inventory':self.inventory,
			'promotion_price':self.promotion_price,
			'start_time':self.start_time,
			'end_time':self.end_time,
			'state':self.state,
			'limit_num':self.limit_num,
			'factory_ID':self.factory_ID,
			'supplier_ID':self.supplier_ID
		}



