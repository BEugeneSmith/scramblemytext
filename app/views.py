from app import app
from app.manipulate import Name
# from app.forms import NameForm
from flask import render_template,redirect,url_for,request
# from flask.ext.bootstrap import Bootstrap
from twilio import twiml

# bootstrap = Bootstrap(app)


@app.route('/',methods=['POST'])
def index():
    response = twiml.Response()
    body = request.form['Body']

    response.message("You sent me: {0}".format(body))

    return str(response)

# @app.route('/scramble/<name>')
# def scramble(name):
#     name = Name(name)
#     return render_template('scramble.html',name=name)
