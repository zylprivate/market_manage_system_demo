#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   crud.py

@Time    :   2020/12/31 19:37

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from .base import db

def insert(model):
	with db.auto_commit_db():
		db.session.add(model)
	# try:
	# 	db.session.commit()
	# except Exception as e:
	# 	print(e)
	# 	db.session.rollback()
	# 	return 0
	# return 1

def delete(model):
	with db.auto_commit_db():
		db.session.delete(model)

'''
ID:用于搜索要修改的字段【primary key】
**params: 要修改的字段 格式为字典{字段名：新字段值}
'''
def update(model, ID, **params):
	new = model.query.get(ID)
	# 遍历出入的参数，并更新对应值
	for key, value in params.items():
		if value:
			setattr(new, key, value)
	with db.auto_commit_db():
		db.session.add(new)
		# 便于判断是否更新成功
		return new
'''
model 对象序列化
return [{},]
'''
def serialize_dict(model):
	dicts=[]
	for m in model:
		m=m.todict()
		dicts.append(m)
	return dicts