from flask import Flask,request,redirect,flash,render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, sample,randint
from stories import story


app = Flask(__name__)

app.config['SECRET_KEY'] = 'chicken'
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def show_story():
    

    text = story.generate(request.args)

    return render_template("story.html", text=text)
