from app import app
from app.textManipulate import Text
from app.forms import TextForm
from flask import render_template,redirect,url_for,request
from flask.ext.bootstrap import Bootstrap
from twilio import twiml

bootstrap = Bootstrap(app)


@app.route('/',methods=['GET','POST'])
def index():
    form = TextForm()
    if form.is_submitted():
        return redirect(url_for('scramble',text=form.text.data))
    return render_template('index.html',form=form)

@app.route('/scramble/<text>')
def scramble(text):
    text = Text(text)
    return render_template('scramble.html',text=text)

@app.route('/sms',methods=['POST'])
def sms():
    response = twiml.Response()
    body = request.form['Body']

    text = Text(body)

    response.message("\npig latin:{0},\nbackwards:{1}".format(text.piglatin(),text.backwards()))
    return str(response)
