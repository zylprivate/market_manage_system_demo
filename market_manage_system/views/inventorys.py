#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   inventorys.py

@Time    :   2021/1/5 16:24

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from  flask import  Blueprint,request,render_template,redirect,url_for
from ..models.crud import insert,update,delete,serialize_dict
from ..models.good_info import Goods
from .auth import login_required,forbidden_page
inventory_bp=Blueprint('inventory',__name__)
@inventory_bp.route('/inventory_manage',methods=('GET', 'POST'))
@login_required
@forbidden_page
def inventory_manage():
	if request.method == 'POST':
		ID = request.form['ID']
		name = request.form['name']
		inventory = request.form['inventory']
		operation = request.form['operation']
		if operation == 'update':
			update(Goods, ID, name=name, inventory=inventory)
		else:
			goods = Goods.query.get(ID)
			delete(goods)
	goods=Goods.query.all()
	goods_info=serialize_dict(goods)
	return  render_template('inventory.html',goods_info=goods_info)
