
from datetime import datetime
from flask import render_template
from gong_web import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        year = datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title = 'About GONG',
        year = datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title = 'GONG Masters',
        year = datetime.now().year
    )

@app.route('/recent-events')
def recent_events():
    """Renders the past events page."""
    return render_template(
        'recent-events.html',
        title='Events',
        year=datetime.now().year,
        message='Events Page.'
    )

@app.route('/swag')
def swag():
    """Renders the merchandise page."""
    return render_template(
        'swag.html',
        title='SWAG',
        year=datetime.now().year,
        message='Your merchandise page.'
    )
