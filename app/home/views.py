# app/home/views.py

from flask import render_template
from flask_login import login_required
from forms import LoginForm

from . import home

@home.route('/')
def home():
    """
    Render the homepage template on the / route
    """
    form = LoginForm()
    return render_template('home/index.html', title="Welcome", form=form)