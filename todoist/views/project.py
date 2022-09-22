from todoist import db
from flask import Blueprint, redirect, url_for, render_template
from todoist.forms.project import ProjectCreationForm
from todoist.forms.task import TaskCreationForm
from todoist.models.project import Project
from flask_login import current_user, login_required
from todoist.models.task import Task

project = Blueprint("project", __name__)

@project.route("/create", methods=["POST"])
@login_required
def create_project():
    form = ProjectCreationForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data, user_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("index"))

@project.route("/<int:project_id>", methods=["GET"])
@login_required
def project_detail(project_id):
    projects = current_user.projects
    project_creation_form = ProjectCreationForm()
    task_creation_form = TaskCreationForm()
    project = Project.query.filter_by(id=project_id).first()
    tasks = project.tasks
    return render_template("dashboard.html", title=project.name, tasks=tasks, project=project, project_creation_form=project_creation_form, task_creation_form=task_creation_form, projects=projects)

@project.route("/<int:project_id>/delete", methods=["POST"])
@login_required
def delete_project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))

@project.route("/<int:project_id>/task/create", methods=["POST"])
@login_required
def create_task(project_id):
    form = TaskCreationForm()
    if form.validate_on_submit():
        project = Project.query.filter_by(id=project_id).first()
        task = Task(body=form.body.data, deadline=form.deadline.data, user_id=current_user.id, project_id=project.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("project.project_detail", project_id=project.id))
        
@project.route("/tasks/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()

@project.route("/deadline/today", methods=["GET"])
@login_required
def tasks_today():
    projects = current_user.projects
    project_creation_form = ProjectCreationForm()
    task_creation_form = TaskCreationForm()
    tasks = Task.query.filter_by(deadline="Today", user_id=current_user.id).all()
    return render_template("dashboard.html", deadline="Today", tasks=tasks, project_creation_form=project_creation_form, task_creation_form=task_creation_form, projects=projects)

@project.route("/deadline/next_week", methods=["GET"])
@login_required
def tasks_next_week():
    projects = current_user.projects
    project_creation_form = ProjectCreationForm()
    task_creation_form = TaskCreationForm()
    tasks = Task.query.filter_by(deadline="Next Week", user_id=current_user.id).all()
    return render_template("dashboard.html", deadline="Next Week", tasks=tasks, project_creation_form=project_creation_form, task_creation_form=task_creation_form, projects=projects)

@project.route("/deadline/this_week", methods=["GET"])
@login_required
def tasks_this_week():
    projects = current_user.projects
    project_creation_form = ProjectCreationForm()
    task_creation_form = TaskCreationForm()
    tasks = Task.query.filter_by(deadline="This Week", user_id=current_user.id).all()
    return render_template("dashboard.html", deadline="This Week", tasks=tasks, project_creation_form=project_creation_form, task_creation_form=task_creation_form, projects=projects)
