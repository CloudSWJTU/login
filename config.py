SECRET_KEY = 'kk17070212'

# MySQL所在的主机名
HOSTNAME = '127.0.0.1'
# MySQL监听的端口号，默认3306
PORT = '3306'
# 连接MySQL的用户名，读者用自己设置的
USERNAME = "root"
# 连接MySQL的密码，读者用自己的
PASSWORD = "kk170702"
# MySQL上创建的数据库名称
DATABASE = "firsttry"
DB_URI="mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

#akgnzzviikcuiece
#邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = '1078240017@qq.com'
MAIL_PASSWORD = 'akgnzzviikcuiece'
MAIL_DEFAULT_SENDER = '1078240017@qq.com'
