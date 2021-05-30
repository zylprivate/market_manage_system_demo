#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   test.py

@Time    :   2020/12/31 16:00

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from contextlib import contextmanager
@contextmanager
def t(a,flag):
	try:
		yield
		b=1/a
	except Exception as e:
		print(e)
def test1():
	a=1
	flag=0
	with t(a,flag) :
		print(flag)
		return 0
if __name__ == '__main__':
	# p=test1()
	# print(p)
	trade_info={'good_list':[],'sum':0}
	list1={'2':'3'}
	list2 = {'2':'3'}
	m1=1
	m2=2
	trade_info['good_list'].append(list1)
	trade_info['good_list'].append(list2)
	trade_info['sum']+=m1
	print(trade_info)
