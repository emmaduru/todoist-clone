from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from todoist.models.project import Project
from flask_login import current_user

class ProjectCreationForm(FlaskForm):
    name = StringField("Project Name", validators=[DataRequired()])
    submit = SubmitField("Add Project")

    def validate_name(self, name):
        project = Project.query.filter_by(name=name.data, user_id=current_user.id).first()
        if project is not None:
            raise ValidationError("Project Name is already taken.")