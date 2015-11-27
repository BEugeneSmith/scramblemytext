from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from re import search



class TextForm(Form):
    text = StringField('text',validators=[DataRequired()])

    submit = SubmitField('Submit')
