from app_package import db, login_manager
from datetime import datetime
from flask_login import LoginManager, UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    paths = db.relationship('Path', backref='creator', lazy='dynamic')
    steps = db.relationship('Step', backref='creator', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.email)  
        
class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
    
class Path(db.Model):
    __tablename__ = 'path'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    description = db.Column(db.String(400), index=True, unique=False)
    is_public = db.Column(db.Boolean, default=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    steps = db.relationship('Step', backref='path', lazy='dynamic')

    def __repr__(self):
        return '<Path {}>'.format(self.name)

class Step(db.Model):
    __tablename__ = 'step'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(400), unique=False)
    link = db.Column(db.String(2048), unique=False)
    step_order = db.Column(db.Integer, index=True, unique=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path_id = db.Column(db.Integer, db.ForeignKey('path.id'))

    def __repr__(self):
        return '<Step {}>'.format(self.name)  