from flask import Flask
from model import connect_to_db, db, User, Temple, Rating, Phone, Savesearch
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "jgjjghhghvxffdrddtrtjjhjhjvvhghgggg"

@app.route('/')
def index():
	return "Hello"







if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()