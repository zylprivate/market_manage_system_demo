#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   auth_info.py

@Time    :   2020/12/31 14:26

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from werkzeug.security import generate_password_hash
from .base import db
from .staff_info import  Staff
# 可能的原因是 view 里目前只用了Account model 所以只识别该文件，因此需要把其他的model文件导入
# from .good_info import Goods
# from .supplier_info import Supplier
# from .member_info import Member
# from .entry_info import Entry
# from .factory_info import Factory
from .sale_info import Sale
# from .stock_info import Stock
from .trade_info import Trade
class Account(db.Model):
	ID=db.Column(db.INTEGER,primary_key=True)
	username=db.Column(db.String(255))
	password=db.Column(db.String(255))
	authority=db.Column(db.SMALLINT)  # 0 收银员 1 管理员
	staff_ID=db.Column(db.String(255),db.ForeignKey('staff.ID'))
	staff=db.relationship('Staff',backref='account')
	def __init__(self,username,password):
		self.username=username
		self.password=generate_password_hash(password)
		self.authority=0 #默认为零
	def __repr__(self):
		return '<username %r>' % self.username
	def todict(self):
		return {
			'ID':self.ID,
			'username':self.username,
			'password':self.password,
			'authority':self.authority,
			'staff_ID':self.staff_ID
		}








