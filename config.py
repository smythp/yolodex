DEBUG= True
# from key import SECRET_KEY


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

emails_to_cache = [
    'signup_confirmation.html',
]    

UPLOAD_FOLDER = 'uploaded/images'

DATABASE = 'dex.db'
