from app import app
from app.manipulate import Name
from app.forms import NameForm
from flask import render_template,redirect,url_for
from flask.ext.bootstrap import Bootstrap

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
