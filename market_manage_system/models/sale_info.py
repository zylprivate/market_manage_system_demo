#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   sale_info.py

@Time    :   2021/1/3 13:11

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
from .good_info import Goods
class Sale(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	goods_ID=db.Column(db.String(255),db.ForeignKey('goods.ID'))
	number=db.Column(db.INTEGER)
	total_amount=db.Column(db.String(255))
	date=db.Column(db.DATE)
	goods=db.relationship('Goods',backref='sale')
	def __init__(self,ID,goods_ID,number,total_amount,date):
		self.ID=ID
		self.goods_ID=goods_ID
		self.number=number
		self.total_amount=total_amount
		self.date=date
	def __repr__(self):
		return '<sale_ID %r>' % self.ID

