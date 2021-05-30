#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   goods.py

@Time    :   2020/12/30 20:57

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from  flask import  Blueprint,request,redirect,url_for,render_template,flash,session,g
from ..Forms.cashier_forms import cashier_add_form,member_form,cashier_cal_form
from ..models.crud import insert,update,delete,serialize_dict
from ..models.good_info import Goods
from ..models.member_info import Member
from ..models.trade_info import Trade
from ..models.sale_info import Sale
from .auth import login_required
import datetime
import random
import string
import time
goods_bp=Blueprint('goods',__name__)
# 定义全局变量
trade_info={'good_list':[],'sum':0.0}
discount=1
serial_num = 0
money_return = 0
member_ID=0
card_ID=0
money_get=0
sale_list=[]
def global_var_init():
	global trade_info, discount, money_return, serial_num, member_ID, card_ID, money_get,sale_list
	trade_info = {'good_list': [], 'sum': 0.0}
	discount = 1
	serial_num = 0
	money_return = 0
	member_ID = 0
	card_ID = 0
	money_get = 0
	sale_list = []
@goods_bp.route('/goods_enter',methods=('GET', 'POST'))
@login_required
def goods_enter():
	if request.method == 'POST':
		ID = request.form['ID']
		name= request.form['name']
		price = request.form['price']
		bar_code = request.form['bar_code']
		# print(ID,name,price,bar_code)
		good=Goods(ID,name,price,bar_code)
		insert(good)
	goods_info=Goods.query.all()
	goods_info=serialize_dict(goods_info)
	# for i in goods_info:
	# 	for key,value in i.items():
	# 		print(key,value)
	# 如果传参必须指定，否则会报错，传参名即为模板里需要的参数名称
	return render_template('goods_enter.html', goods_info=goods_info)
# 后续移动到trade
@goods_bp.route('/cashier',methods=('GET', 'POST'))
@login_required
def cashier():
	global trade_info,discount,money_return,serial_num,member_ID,card_ID,money_get,sale_list
	add_form=cashier_add_form()
	mem_form=member_form()
	cal_form=cashier_cal_form()
	if mem_form.submit.data and mem_form.validate():
		card_ID=mem_form.card_ID.data
		member=Member.query.filter_by(card_ID=card_ID).first()
		if member:
			member_ID =member.ID
			discount=0.95
			print(discount)
			# 给js alter 显示时间
			time.sleep(0.7)
	if add_form.submit.data and add_form.validate():
		name_or_code=add_form.name_or_code.data
		print(name_or_code)
		# 哪个有结果用那个
		good=Goods.query.filter_by(name=name_or_code).first() or Goods.query.filter_by(bar_code=name_or_code).first()
		print(good)
		good_dict=good.todict()
		good_dict['bar_code']=add_form.num.data
		good_dict['inventory']=float(good.price)*float(discount)*float(add_form.num.data)
		trade_info['good_list'].append(good_dict)
		current_price=float(good.price)*float(discount)    # 后期补上是否促销的判断
		trade_info['sum']+=current_price*float(add_form.num.data)
		print(trade_info)
		sale={'ID':''.join(random.sample(string.ascii_letters + string.digits, 10)),
		       'good_ID':good.ID,
		       'num':add_form.num.data,
		       'total_amount':current_price*float(add_form.num.data),
		       'date':datetime.datetime.now().date()}
		sale_list.append(sale)
	if cal_form.submit.data and cal_form.validate():
		money_get=cal_form.money_get.data
		money_return=float(money_get)-trade_info['sum']
		serial_num=''.join(random.sample(string.ascii_letters + string.digits, 10))
		trade=Trade(serial_num,trade_info['sum'],datetime.datetime.now().date(),member_ID,g.account)
		insert(trade)
		for sale in sale_list:
			sale_=Sale(sale['ID'],sale['good_ID'],sale['num'],sale['total_amount'],sale['date'])
			insert(sale_)
		# 给js alter 显示时间
		time.sleep(0.7)
	return render_template('cashier.html',
	                       add_form=add_form,
	                       mem_form=mem_form,
	                       cal_form=cal_form,
	                       trade_info=trade_info,
	                       card_ID=card_ID
	                       )
@goods_bp.route('/trade_print',methods=('GET', 'POST'))
@login_required
def trade_print():
	current_time=datetime.datetime.now().date()
	trade_info_=trade_info
	current_time_=current_time
	money_get_=money_get
	money_return_=money_return
	serial_num_=serial_num
	member_ID_=member_ID
	card_ID_=card_ID
	global_var_init()
	return render_template('trade_print.html',
	                       trade_info=trade_info_,
	                       current_time=current_time_,
	                       money_get=money_get_,
	                       money_return=money_return_,
	                       serial_num=serial_num_,
	                       member_ID=member_ID_,
	                       card_ID=card_ID_
	                       )


