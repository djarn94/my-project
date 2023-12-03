# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'The boys of IG are nutter then nuts. Now this piece of text should be visible.'

@app.route('/cow')
def cow():
    return 'MOoooOo!'