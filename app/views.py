from app import app
from flask import render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

@app.route('/')
def home():
    return render_template('public/home.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('public/dashboard.html')

