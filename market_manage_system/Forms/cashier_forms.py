#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   cashier_forms.py

@Time    :   2021/1/4 11:15

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from flask_wtf import FlaskForm  # FlaskForm 为表单基类
from wtforms import StringField, PasswordField, SubmitField  # 导入字符串字段，密码字段，提交字段
from wtforms.validators import DataRequired, ValidationError


class cashier_add_form(FlaskForm):
	name_or_code = StringField(
		label='name_or_code',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": "请输入商品名或商品码",
			"required": 'required'  # 表示输入框不能为空，并有提示信息
		})
	num = StringField(
		label='num',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": "请输入商品数量",
			"required": 'required'  # 表示输入框不能为空，并有提示信息
		})
	submit = SubmitField(
		label="加 入",
		render_kw={
			"class": "btn btn-info",
		}
	)


class member_form(FlaskForm):
	card_ID = StringField(
		label='card_ID',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": "如有，请输入会员卡号",
			"required": 'required'
		})
	submit = SubmitField(
		label="扫 描",
		render_kw={
			"class": "btn btn-info swalDefaultSuccess_card",
		}
	)


class cashier_cal_form(FlaskForm):
	money_get = StringField(
		label='money_get',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": "请输入实收款",
			"required": 'required'  # 表示输入框不能为空，并有提示信息
		})
	submit = SubmitField(
		label="结 算",
		render_kw={
			"class": "btn btn-info swalDefaultSuccess_cal",
		}
	)
