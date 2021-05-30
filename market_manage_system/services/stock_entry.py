#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   stock_entry.py

@Time    :   2021/1/5 12:53

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from ..models.good_info import Goods
from ..models.stock_info import Stock
from ..models.entry_info import Entry
from ..models.crud import insert,update
import datetime
import random
import string
# 两个必须时datetime 类型
'''
  time1 >= time2 True
  time1 <  time2 False
'''
def time_comp(time1,time2):
	t=time1-time2
	if t.days<0:
		return False
	else:
		return True
def stocks_serv():
	goods=Goods.query.all()
	for good in goods:
		if good.inventory <10:
			serial_num = ''.join(random.sample(string.ascii_letters + string.digits, 10))
			# 明天进货
			plan_time = datetime.datetime.now()+datetime.timedelta(days=1)
			stock=Stock(serial_num,good.ID,50,plan_time.date(),0)
			insert(stock)
def entrys_serv():
	stocks=Stock.query.all()
	current_time=datetime.datetime.now().date()
	for stock in stocks:
		# print(stock.plan_time)
		# if isinstance(stock.plan_time,str):
		# 	stock.plan_time=datetime.datetime.strptime(stock.plan_time,"%Y-%m-%d")
		# 	print(stock.plan_time)
		if time_comp(current_time,stock.plan_time):
			update(Stock,stock.ID,state=1)
			serial_num = ''.join(random.sample(string.ascii_letters + string.digits, 10))
			# 预计明天能进到货
			plan_time = datetime.datetime.now() + datetime.timedelta(days=1)
			total_amount=float(stock.number)*float(stock.goods.price)
			entry = Entry(serial_num, stock.goods_ID, stock.number, plan_time.date(), 0,total_amount)
			insert(entry)


