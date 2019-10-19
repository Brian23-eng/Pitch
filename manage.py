from app import create_app, db
from flask import Flask
from flask_script import Manager,Server


# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db')

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)

if __name__ == '__main__':
    app.secret_key = 'bran'
    manager.run()