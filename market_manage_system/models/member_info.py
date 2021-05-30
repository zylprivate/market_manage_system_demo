#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   member_info.py

@Time    :   2021/1/3 13:08

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
class Member(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	card_ID=db.Column(db.String(255))
	phone_number=db.Column(db.String(255))
	register_date=db.Column(db.DATE)
	renewal_date=db.Column(db.DATE)
	aggregate_amount=db.Column(db.String(255))
	def __init__(self,ID,card_ID,phone_number,register_date,renewal_date,aggregate_amount):
		self.ID=ID
		self.card_ID=card_ID
		self.phone_number=phone_number
		self.register_date=register_date
		self.renewal_date=renewal_date
		self.aggregate_amount=aggregate_amount
	def __repr__(self):
		return '<member_ID %r>' % self.ID
