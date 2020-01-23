from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)

@app.route('/')
def words_input():
    """ Generate and show form to ask words. """

    prompts = story.prompts

    return render_template('questionstemplate.html', prompts=prompts)

@app.route('/story')
def generate_story():
    """ Generate story from inputs. """

    text = story.generate(request.args)

    return render_template('storytemplate.html', text=text)

