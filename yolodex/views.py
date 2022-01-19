from flask import url_for, request, render_template, abort, flash, render_template_string, current_app, redirect, send_from_directory
from yolodex import app
from .forms import CreateContactForm


@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():



    return render_template('index.html')




@app.route('/add/contact', methods=['GET', 'POST'])
def add_contact():

    form = CreateContactForm(request.form)

    if request.method == 'POST' and form.validate():

        now = datetime.datetime.now()

        last_modified, created = now, now
        birthday = form.birthday.data
        secondary = form.secondary.data
        phone = form.phone.data
        firstname = form.first_name.data
        lastname = form.lastname.data
        middleName = form.middleName.data
        suffix = form.suffix.data
        nickname = form.nickname.data
        gender = form.gender.data
        address_1 = form.address_1.data
        address_2 = form.address_2.data
        city = form.city.data
        zip = form.zip.data
        title = form.title.data
        email = form.email.data
        notes = form.notes.data
       
        flash('Contact added')

        return render_template('add_contact.html',
                               form=form)


    return render_template('add_contact.html',
                           form=form)        



