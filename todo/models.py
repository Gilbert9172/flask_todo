from todo import db

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='Todo')
    title = db.Column(db.String(100))
    desc = db.Column(db.Text())
    complete = db.Column(db.Boolean)
