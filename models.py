from flask_sqlalchemy import SQLAlchemy
from main import app


db = SQLAlchemy(app)


def create_app():
    db.init_app(app)
    db.create_all()
    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr(self):
        return "<Model User - {}>".format(self.name)


