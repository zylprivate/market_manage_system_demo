#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   purchase.py

@Time    :   2020/12/30 21:00

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from  flask import  Blueprint,request,render_template,redirect,url_for
from ..models.crud import insert,update,delete,serialize_dict
from ..models.entry_info import Entry
from ..models.stock_info import Stock
from .auth import login_required,forbidden_page
from ..services.stock_entry import stocks_serv,entrys_serv

import datetime
purchase_bp=Blueprint('purchase',__name__)


@purchase_bp.route('/purchase_plan',methods=('GET', 'POST'))
@login_required
@forbidden_page
def purchase_plan():
	if request.method == 'POST':
		ID = request.form['ID']
		goods_ID= request.form['goods_ID']
		number = request.form['number']
		plan_time = request.form['plan_time']
		if plan_time:
			plan_time=datetime.datetime.strptime(plan_time,"%m/%d/%Y").date()
		else:
			plan_time=datetime.datetime.now().date()
		# print(plan_time)
		state = 0
		operation = request.form['operation']
		#current_time = datetime.datetime.now().date()
		#print(operation)
		if operation=='add':
			stock=Stock(ID,goods_ID,number,plan_time,state)
			insert(stock)
		elif operation=='update':
			update(Stock,ID,goods_ID=goods_ID,number=number,plan_time=plan_time,state=state)
		else:
			stock=Stock.query.get(ID)
			delete(stock)
	stocks_info=Stock.query.all()
	stocks_info=serialize_dict(stocks_info)
	return render_template('purchase_plan.html',stocks_info=stocks_info)
@purchase_bp.route('/purchase_goods',methods=('GET', 'POST'))
@login_required
@forbidden_page
def purchase_goods():
	if request.method == 'POST':
		ID = request.form['ID']
		goods_ID= request.form['goods_ID']
		number = request.form['number']
		time = request.form['time']
		state = request.form['state']
		if state is None:
			state=0
		operation = request.form['operation']
		if time:
			time = datetime.datetime.strptime(time, "%m/%d/%Y").date()
		else:
			time=datetime.datetime.now().date()
		#current_time = datetime.datetime.now().date()
		#print(operation)
		if operation=='add':
			entry=Entry(ID,goods_ID,number,time,state)
			insert(entry)
		elif operation=='update':
			update(Entry,ID,goods_ID=goods_ID,number=number,time=time,state=state)
		else:
			entry=Entry.query.get(ID)
			delete(entry)
	entrys_info=Entry.query.all()
	entrys_info=serialize_dict(entrys_info)
	return render_template('purchase_goods.html',entrys_info=entrys_info)
@purchase_bp.route('/stock_check')
@login_required
@forbidden_page
def stock_check():
	stocks_serv()
	return redirect(url_for('purchase.purchase_plan'))
@purchase_bp.route('/entry_check')
@login_required
@forbidden_page
def entry_check():
	entrys_serv()
	return redirect(url_for('purchase.purchase_goods'))

