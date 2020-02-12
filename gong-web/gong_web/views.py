
from datetime import datetime
from flask import render_template
from gong_web import app

import httplib2
import os
from apiclient import discovery
from google.oauth2 import service_account

#import gspread
#from oauth2client.service_account import ServiceAccountCredentials

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        year = datetime.now().year
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
    return render_template(
        'swag.html',
        title = 'SWAG',
        year = datetime.now().year
    )

@app.route('/recent-events')
def recent_events():
    """Renders the past events page."""

    ## Pasted in below

    scopes = ["https://www.googleapis.com/auth/drive", 
              "https://www.googleapis.com/auth/drive.file", 
              "https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), 'Credentials\\client_secret.json')  # Might have to change to \\

    spreadsheet_id = '1eP_ZRzV81KMMiofMP7XV_TBUYGLAckKBzLqzPPBpNnk'  # Change to mine
    #range_name = 'Sheet1!A1:D2'
    
    # Producing the wrong file path
    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes = scopes)
    service = discovery.build('sheets', 'v4', credentials = credentials)

    ## Pasted in above

    data = client.open('GONG-events').sheet1

    return render_template(
        'recent-events.html',
        title='Events',
        year=datetime.now().year,
        message='Events Page.'
    )

