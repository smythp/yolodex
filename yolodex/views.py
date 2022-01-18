from flask import url_for, request, render_template, abort, flash, render_template_string, current_app, redirect, send_from_directory
from yolodex import app



@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')
