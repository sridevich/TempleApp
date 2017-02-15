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
def register_form():
    """Show form for new user registration."""

    return render_template("register.html")


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

    new_user = User(email=email, pass_word=pass_word, first_name=first_name, last_name=last_name, 
    				address=address, city=city, state=state)

    #print new_user
    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/login")

@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    pass_word = request.form["pass_word"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user.  Please register!")
        return redirect("/register")

    if user.pass_word != pass_word:
        flash("Incorrect Password! Please enter correct password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect("/")
    #return redirect("/users/%s" % user.user_id)

@app.route('/search')
def search_form():
    """ Show list of Temples form. """

    state = request.args.get("state")
    zipcode = request.args.get("zipcode")

    searches = db.session.query(Temple.t_name, Temple.address,
                Temple.city, Temple.state, Temple.zipcode,
                Phone.phone_no_1).join(Phone).all()


    return render_template("temple_list.html", searches=searches)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")