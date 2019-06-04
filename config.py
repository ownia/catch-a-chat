# 配置
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # Flask使用SECRET_KEY作为加密密钥用于生成签名或者令牌
    # Flask-WTF使用它来保护web表单免于CSRF的攻击。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Flask-SQLAlchemy扩展从SQLALCHEMY_DATABASE_URI配置变量中获取应用程序数据库的位置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 添加Email服务器信息
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['o451686892@outlook.com']
    # POSTS_PER_PAGE决定了每次返回文章列表的条目数
    POSTS_PER_PAGE = 10
    # list of tracked language
    LANGUAGES = ['en', 'zh']
    # 配置Elasticsearch
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # 配置Redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    #
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
