from flask import Flask, current_app
from config import DATABASE, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
import os
from datetime import datetime
from babel.dates import format_datetime as babel_format_datetime

app = Flask(__name__)
app.config.from_object('config')



app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, UPLOAD_FOLDER)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000



def load_user(id):

    db = DataAccess(current_app.config['DATABASE'])

    user = db.get('users', 'id', id)


    if user:
        user_out = User(user['username'], user['id'])
    else:
        user_out = None

    return user_out



@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}




@app.template_filter()
def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel_format_datetime(value, format)
    


from yolodex import views
