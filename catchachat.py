from app import app, db
from app.models import User, Post


# app.shell_context_processor decorator将该函数注册为shell上下文函数
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
