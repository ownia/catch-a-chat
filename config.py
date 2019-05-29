# 配置
import os


class Config(object):
    # Flask使用SECRET_KEY作为加密密钥用于生成签名或者令牌
    # Flask-WTF使用它来保护web表单免于CSRF的攻击。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
