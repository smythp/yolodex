from yolodex import app
# from config import SECRET_KEY


# app.config.from_object('config')



# app.config['SECRET_KEY'] = SECRET_KEY

app.config['testing'] = False


def create_app():

    return app

