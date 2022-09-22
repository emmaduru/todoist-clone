from todoist import app
from flask_login import login_required
from flask import render_template
from todoist.forms.project import ProjectCreationForm
from flask_login import current_user
from todoist.forms.task import TaskCreationForm
from todoist.models.task import Task

@app.route("/")
@login_required
def index():
    projects = current_user.projects
    tasks = current_user.tasks
    project_creation_form = ProjectCreationForm()
    task_creation_form = TaskCreationForm()
    return render_template("dashboard.html", title="Dashboard", tasks=tasks, task_creation_form=task_creation_form, project_creation_form=project_creation_form, projects=projects)