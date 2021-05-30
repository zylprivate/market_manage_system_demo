#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   manage.py

@Time    :   2020/12/30 21:00

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from  flask import  Blueprint,render_template,request
from ..models.crud import insert,update,delete,serialize_dict
from ..models.staff_info import Staff
from ..models.factory_info import Factory
from .auth import login_required,forbidden_page
import datetime
# 后期重构更换成people
manage_bp=Blueprint('manage',__name__)
@manage_bp.route('/manage_people',methods=('GET', 'POST'))
@login_required
@forbidden_page
def manage_people():
	if request.method == 'POST':
		ID = request.form['ID']
		name= request.form['name']
		sex = request.form['sex']
		title = request.form['title']
		state = request.form['state']
		operation = request.form['operation']
		current_time = datetime.datetime.now().date()
		work_age=0
		print(operation)
		if operation=='add':
			staff=Staff(ID,name,sex,title,state,current_time,work_age)
			insert(staff)
		elif operation=='update':
			update(Staff,ID,name=name,sex=sex,title=title,state=state)
		else:
			staff=Staff.query.get(ID)
			delete(staff)
	staffs_info=Staff.query.all()
	staffs_info=serialize_dict(staffs_info)
	return render_template('manage_people.html',staffs_info=staffs_info)
@manage_bp.route('/manage_factory',methods=('GET', 'POST'))
@login_required
@forbidden_page
def manage_factory():
	if request.method == 'POST':
		ID = request.form['ID']
		name= request.form['name']
		address = request.form['address']
		telephone = request.form['telephone']
		operation = request.form['operation']
		print(operation)
		if operation=='add':
			factory=Factory(ID,name,address,telephone)
			insert(factory)
		elif operation=='update':
			update(Factory,ID,name=name,address=address,telephone=telephone)
		else:
			factory=Factory.query.get(ID)
			delete(factory)
	factorys_info=Factory.query.all()
	factorys_info=serialize_dict(factorys_info)
	return render_template('manage_factory.html',factorys_info=factorys_info)