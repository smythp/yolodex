from wtforms import Form, IntegerField, BooleanField, StringField, PasswordField, DateField, TimeField, validators
from wtforms.widgets import TextArea
from flask_login import current_user
from slugify import slugify
from datetime import datetime


class CreateContactForm(Form):

    first_name = StringField('First Name', [
        validators.DataRequired(),
        ])


    birthday = TimeField('Birthday', [
        validators.DataRequired(),
    ])


    secondary = BooleanField('Secondary Contact?', [
           validators.DataRequired(),
       ])
       
    phone = IntegerField('Phone', [
        validators.DataRequired(),
    ])

    
    first_name = StringField('First Name', [
        validators.DataRequired(),
    ])

    last_name = StringField('Last Name', [
        validators.DataRequired(),
    ])

    middle_name = StringField('Middle Name', [
        validators.DataRequired(),
    ])

    suffix = StringField('Suffix', [
        validators.DataRequired(),
    ])

    nickname = StringField('Nickname', [
        validators.DataRequired(),
    ])

    gender = StringField('Gender', [
        validators.DataRequired(),
    ])

    address_1 = StringField('Address 1', [
        validators.DataRequired(),
    ])

    address_2 = StringField('Address 2', [
        validators.DataRequired(),
    ])

    city = StringField('City', [
        validators.DataRequired(),
    ])

    zip = StringField('Zip', [
        validators.DataRequired(),
    ])

    title = StringField('Title', [
        validators.DataRequired(),
    ])
    email = StringField('Email', [
        validators.DataRequired(),
    ])

    notes = StringField('Notes',
                        [validators.Length(min=6, max=150000)],
                        widget=TextArea())



    # def validate_name(form, field):

        # id = current_user.id
        # slug = slugify(field.data)

        # if resource_exists_validator('iotas', id, slug):
        #     raise validators.ValidationError('You have already created an iota with that name. Try something different')


