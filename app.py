from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app=Flask("__madlibs__")

app.debug = True
app.config['SECRET_KEY'] = 'my_key'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def main_page():
    libs = story.prompts
    text = story.template
    return render_template("main.html", my_libs = libs, my_text = text )


@app.route('/story', methods=['POST'])
def story_page():   
    
    answers = {"place" : request.form["place"],
    "noun" : request.form["noun"],
    "verb" :request.form["verb"],
    "adjective" :request.form["adjective"],
    "plural_noun" :request.form["plural_noun"]}

    finished_sentence = story.generate(answers)

    return render_template("story.html",  finished_sentence =finished_sentence )