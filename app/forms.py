from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class TextForm(Form):
    text = StringField('text',validators=[Required()])

    submit = SubmitField('Submit')
