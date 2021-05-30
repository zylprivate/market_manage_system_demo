#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   auth.py

@Time    :   2020/12/30 20:30

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from  flask import  Blueprint,request,redirect,url_for,render_template,flash,session,g
from werkzeug.security import check_password_hash,generate_password_hash
import  functools
from ..models.auth_info import  Account
from ..models.crud import insert,update,delete
auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		info = None
		# 前端判别就行
		# if not username:
		# 	error = 'Username is required.'
		# elif not password:
		# 	error = 'Password is required.'
		account=Account.query.filter_by(username=username).first()
		if account:
			print('User {} is already registered.'.format(username))
			info = 'User {} is already registered.'.format(username)
		else:
			account=Account(username,password)
			insert(account)
			return redirect(url_for('auth.login'))
		flash(info,'warning')
	return render_template('register.html')

@auth_bp.route('/login',methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		info = None
		account = Account.query.filter_by(username=username).first()
		if not account:
			print('Incorrect username.')
			info = 'Incorrect username.'
		elif not check_password_hash(account.password, password):
			info = 'Incorrect password.'
		else:
			session.clear()
			session['account_ID'] = account.ID
			if account.authority :
				return redirect(url_for('manage.manage_people'))
			else:
				return redirect(url_for('goods.goods_enter'))
		flash(info,'warning')
	return render_template('login.html')
'''
before_app_request 注册一个 在视图函数之前运行的函数，不论其 URL 是什么。
load_logged_in_user 检查用户 id 是否已经储存在 session 中，
并从数据库中获取用户数据，然后储存在 g.user 中。 g.user 的持续时间比请求要长。
如果没有用户 id ，或者 id 不存在，那么 g.user 将会是 None 。
'''
@auth_bp.before_app_request
def load_logged_in_user():
	account_ID = session.get('account_ID')
	if account_ID is None:
		g.account = None
	else:
		g.account = Account.query.get(account_ID)

@auth_bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('mains.welcome'))

'''
构建一个装饰器，装饰器返回一个新的视图，
该视图包含了传递给装饰器的原视图。新的函数检查用户 是否已载入。
如果已载入，那么就继续正常执行原视图，否则就重定向到登录页面。
'''
def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.account is None:
			return redirect(url_for('auth.login'))
		return view(**kwargs)
	return wrapped_view

def forbidden_page(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.account.authority is 0:
			return render_template('403.html')
		return view(**kwargs)

	return wrapped_view