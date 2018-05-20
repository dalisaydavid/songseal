# app/recommendations/views.py

from flask import render_template

from . import recommendations

@recommendations.route('/recommendations')
def recommendations():
    """
    Render the homepage template on the / route
    """
    return render_template('recommendations/index.html', title="Welcome")