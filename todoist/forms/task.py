from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from todoist.models.task import Task
# from flask_login import current_user

class TaskCreationForm(FlaskForm):
    body = StringField("Task", validators=[DataRequired()])
    deadline = SelectField("Deadline", default="Today", choices=[("Today", "Today"), ("This Week", "This Week"), ("Next Week", "Next Week")])
    submit = SubmitField("Add Task")