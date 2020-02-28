from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    name = db.Column(db.String(120), unique=False, nullable=True)
    todos = db.relationship('Todos', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username
    def serialize_todos(self):
        return list(map(lambda x: x.serialize(), self.todos))

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
             "todos": list(map(lambda x: x.serialize(), self.todos))
        }

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(250), nullable=False)
    done = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return '<Todo for user with ID %r>' % self.user_id

    def serialize(self):
        return dict(
            label = self.label,
            done = self.done
        )