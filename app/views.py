from app import app
from app.manipulate import Name
from app.forms import NameForm
from flask import render_template,redirect,url_for,request
from flask.ext.bootstrap import Bootstrap
from twilio import twiml

bootstrap = Bootstrap(app)


@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.is_submitted():
        return redirect(url_for('scramble',name=form.name.data))
    return render_template('index.html',form=form)

@app.route('/scramble/<name>')
def scramble(name):
    name = Name(name)
    return render_template('scramble.html',name=name)

@app.route('/sms',methods=['POST'])
def sms():
    response = twiml.Response()
    body = request.form['Body']

    name = Name(body)

    response.message("\npig latin:{0},\nbackwards:{1}".format(name.piglatin(),name.backwards()))
    return str(response)
