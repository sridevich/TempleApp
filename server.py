""" Search Temples. """

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Temple, Rating, Phone, Savesearch


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "jgjjghhghvxffdrddtrtjjhjhjvvhghgggg"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	
	return render_template("home.html")

@app.route('/register', methods=['GET'])
def registeration_form():
    """Show form for new user registration."""

    return render_template("registeration.html")


@app.route('/register', methods=['POST'])
def registeration_process():
    """Process registration."""

    # Get form variables
    email = request.form["email"]
    pass_word = request.form["password"]
    first_name=request.form["firstname"]
    last_name=request.form["lastname"]
    address = request.form["address"]
    city = request.form["city"]
    state = request.form["state"]
    zipcode = request.form["zipcode"]

    new_user = User(email=email, password=pass_word, first_name=firstnamme, last_name=lastname, 
    				address=address, city=city, state=state, zipcode=zipcode)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/")

@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect("/users/%s" % user.user_id)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()