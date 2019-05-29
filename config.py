# 配置
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Flask使用SECRET_KEY作为加密密钥用于生成签名或者令牌
    # Flask-WTF使用它来保护web表单免于CSRF的攻击。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Flask-SQLAlchemy扩展从SQLALCHEMY_DATABASE_URI配置变量中获取应用程序数据库的位置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
