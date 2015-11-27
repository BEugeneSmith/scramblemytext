from app import app
from app.textManipulate import TextTransform
from app.VizGenerate import SVG
from app.forms import TextForm,hasNumbers
from flask import render_template,redirect,url_for,request
from flask.ext.bootstrap import Bootstrap
from twilio import twiml

bootstrap = Bootstrap(app)


@app.route('/',methods=['GET','POST'])
def index():
    form = TextForm()
    if form.is_submitted():
        if hasNumbers(form.text):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('scramble',text=form.text.data))
    return render_template('index.html',form=form)

@app.route('/scramble/<text>')
def scramble(text):
    text = TextTransform(text)
    svg = SVG(text.text)

    return render_template('scramble.html',text=text,svg=svg.SVG)

@app.route('/sms',methods=['POST'])
def sms():
    response = twiml.Response()
    text = Text(request.form['Body'])

    response.message("\npig latin:{0},\nbackwards:{1}".format(text.piglatin(),text.backwards()))
    return str(response)
