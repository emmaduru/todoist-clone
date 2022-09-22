from todoist import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from todoist import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String)
    projects = db.relationship("Project", backref="user", lazy=True, cascade="all, delete")
    tasks = db.relationship("Task", backref="user", lazy=True, cascade="all, delete")

    def __repr__(self):
        return "<User {}>".format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
