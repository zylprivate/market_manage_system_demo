#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   purchase_forms.py

@Time    :   2021/1/5 13:45

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from flask_wtf import FlaskForm  # FlaskForm 为表单基类
from wtforms import StringField, PasswordField, SubmitField  # 导入字符串字段，密码字段，提交字段
from wtforms.validators import DataRequired, ValidationError
class plan_form(FlaskForm):
	ID = StringField(
		label='ID',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": "",
			"required": 'required'  # 表示输入框不能为空，并有提示信息
		})
	goods_ID = StringField(
		label='goods_ID',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": ""
		})
	number = StringField(
		label='number',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": ""
		})
	plan_time = StringField(
		label='plan_time',
		validators=[DataRequired()],
		render_kw={
			"class": "form-control",
			"placeholder": ""
		})
	submit = SubmitField(
		label="加 入",
		render_kw={
			"class": "btn btn-info",
		}
	)
