from flask import Blueprint, render_template, url_for


blp = Blueprint('routes','routes')

@blp.route('/')
def home():
    appList = [
        {'name': 'Work', 'route':'iwork','image_url':url_for('static', filename='assets/images/work.png')}
    ]
    return render_template('index.html', appList = appList)

@blp.route('/favicon.ico')
def favicon():
    return url_for('static', filename='assets/favicon.ico') 