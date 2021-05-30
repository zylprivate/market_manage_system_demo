#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   trade_info.py

@Time    :   2021/1/3 13:09

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db
from .staff_info import Staff
from .member_info import Member
class Trade(db.Model):
	ID=db.Column(db.String(255),primary_key=True)
	amount=db.Column(db.String(255))
	time=db.Column(db.DATETIME)
	member_ID=db.Column(db.String(255),db.ForeignKey('member.ID'))
	staff_ID=db.Column(db.String(255),db.ForeignKey('staff.ID'))
	member=db.relationship('Member',backref='trade')
	staff=db.relationship('Staff',backref='trade')
	def __init__(self,ID,amount,time,member_ID,staff_ID):
		self.ID=ID
		self.amount=amount
		self.time=time
		self.member_ID=member_ID
		self.staff_ID=staff_ID
	def __repr__(self):
		return '<trade_ID %r>' % self.ID
