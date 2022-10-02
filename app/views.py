from app import app
from flask import render_template
from flask_login import login_required

@app.route('/')
def home():
    return render_template('public/home.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('public/dashboard.html')

