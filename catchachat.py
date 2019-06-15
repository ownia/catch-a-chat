# coding=UTF-8
from app import db, cli, create_app
from app.models import User, Post, Message, Notification, Task

app = create_app()
cli.register(app)


# app.shell_context_processor decorator将该函数注册为shell上下文函数
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, "Message": Message, "Notification": Notification, "Task": Task}
