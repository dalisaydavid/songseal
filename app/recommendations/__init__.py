# app/recommendations/__init__.py

from flask import Blueprint

recommendations = Blueprint('recommendations', __name__)

from . import views