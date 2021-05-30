#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   run.py

@Time    :   2020/12/30 9:53

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''

from  market_manage_system import  create_app

if __name__ == '__main__':
	app= create_app()
	app.run()
