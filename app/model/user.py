from email.policy import default
from enum import auto
from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)