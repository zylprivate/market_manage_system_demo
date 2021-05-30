SECRET_KEY = 'Sm5obiBTY2htb70ga2lja4MgYXNz'
# 'mysql+pymysql://用户名称:密码@目标主机ip:端口/数据库名称' 【本地主机ip为localhost】
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskweb:En23yRfCWzPGYDtr@47.101.47.223:3306/flaskweb'
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_ECHO = True