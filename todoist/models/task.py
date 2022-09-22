from enum import Enum
from todoist import db


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    deadline = db.Column(db.Enum("Today", "This Week", "Next Week"), server_default="Today")
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Task {}>".format(self.body)