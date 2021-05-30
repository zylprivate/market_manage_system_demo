#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   __init__.py.py

@Time    :   2020/12/30 9:55

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from .mains import mains_bp
from .auth import auth_bp
from .purchase import purchase_bp
from .trading import trading_bp
from .goods import goods_bp
from .sales import sales_bp
from .manage import manage_bp
from .inventorys import inventory_bp
def init_app(app):
	app.register_blueprint(mains_bp)
	app.register_blueprint(auth_bp)
	app.register_blueprint(purchase_bp)
	app.register_blueprint(trading_bp)
	app.register_blueprint(goods_bp)
	app.register_blueprint(sales_bp)
	app.register_blueprint(manage_bp)
	app.register_blueprint(inventory_bp)

