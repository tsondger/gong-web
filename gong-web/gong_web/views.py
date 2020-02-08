
from datetime import datetime
from flask import render_template
from gong_web import app
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials

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

@app.route('/swag')
def swag():
    """Renders the merchandise page."""
    
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    #creds = ServiceAccountCredentials.from_json_keyfile_name('../static/credentials/gong-secret.json', scope)
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:/gong-web/gong-web/gong-web/gong_web/static/credentials/gong-creds.json', scope)  # Need a relative file path 
    client = gspread.authorize(creds)  # Getting an error about it not being used in a project before or disabled, don't think I'm enabling it correctly in the project

    data = client.open('GONG-events').sheet1
    
    return render_template(
        'swag.html',
        title = 'SWAG',
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

