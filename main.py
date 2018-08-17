from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

from config import DevConfig # 引入配置文件

app = Flask(__name__)
# 通过配置文件读取并应用配置
app.config.from_object(DevConfig)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()