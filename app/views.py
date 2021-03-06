from app import app
from app.textManipulate import TextTransform
from app.D3Preparation import CreateDataset
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
    text = TextTransform(text)
    ds = CreateDataset(text.text)

    return render_template('scramble.html',text=text,json=ds.ds)

@app.route('/sms',methods=['POST'])
def sms():
    response = twiml.Response()
    text = Text(request.form['Body'])

    response.message("\npig latin:{0},\nbackwards:{1}".format(text.piglatin(),text.backwards()))
    return str(response)
