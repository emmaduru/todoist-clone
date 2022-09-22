import os
basedir = os.path.dirname(__file__)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLITE_DB") or "sqlite:///" + os.path.join(basedir, "todoist.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True