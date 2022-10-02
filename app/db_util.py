from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)