#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   manage.py

@Time    :   2021/1/2 10:23

@Author  :   Waking

@Contact :   ylzhangcs@hotmail.com
'''
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from market_manage_system.models import db
from market_manage_system import create_app
app=create_app()
manage=Manager(app)
migrate=Migrate(app,db)
manage.add_command("db",MigrateCommand)
if __name__ == '__main__':
	manage.run()
