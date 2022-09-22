from todoist import db

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tasks = db.relationship("Task", backref="project", lazy=True, cascade="all, delete")

    def __repr__(self):
        return "<Project {}>".format(self.name)