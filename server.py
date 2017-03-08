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
    zipcode = request.form["zipcode"]
    phone = request.form["phone"]
    age = request.form["age"]

    new_user = User(email=email, pass_word=pass_word, first_name=first_name, last_name=last_name, 
    				address=address, city=city, state=state, zipcode=zipcode, phone=phone, age=age)

    #print new_user
    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/temple_list.html")

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
    #return redirect("/")
    return redirect("/users/%s" % user.user_id)
    #return redirect("/search")


@app.route("/logout")
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out!")
    return redirect("/")


@app.route('/search')
def temple_search_form():
    """ Show list of Temples form. """

    state = request.args.get("state")
    print state
    zipcode = request.args.get("zipcode")
    print zipcode
    temples = Temple.query.filter_by(state=state, zipcode=zipcode).all()
    print temples

    # # temples = db.session.query(Temple.t_name, Temple.address,
    # #             Temple.city, Temple.state, Temple.zipcode,
    # #             Phone.phone_no_1).join(Phone).filter(Temple.state==state, Temple.zipcode==zipcode).all()

    return render_template("temple_list.html", temples=temples)

    

@app.route("/users/<int:user_id>")
def user_profile(user_id):
    """Show user information."""

    user = User.query.get(user_id)
    return render_template("user.html", user=user, temple_id=session["temple_id"])

@app.route("/temple/<temple_id>")
def temple_profile(temple_id):

    temple = Temple.query.get(temple_id)
    #import pdb; pdb.set_trace()
    user = session.get("user_id")

    session["temple_id"] = temple_id
    return render_template("temple.html", temple=temple, user_id=user, temple_id=session["temple_id"])
    

@app.route("/savetemple", methods=["POST"])
def savetemple():
    """ saves user search """
    savetemple = request.form.get("templeid")

    user = session.get("user_id")

    if not user:

        db.session.add(Savesearch(temple_id=savetemple, user_id=user))
        db.session.commit()
        flash("Saved temple")
    else:

        flash("Already saved!")


    return redirect("/temple/" + savetemple)

@app.route("/saveratings", methods=["POST"])
def saveratings():
    """saves user ratings """
    # Get form variables

    temple_id=request.form.get("templeid")
    score = int(request.form.get("score"))
    user = session.get("user_id")
    comments = request.form.get("comments")
    
    rating = Rating.query.filter_by(user_id=user, temple_id=temple_id).first()

    if rating:
        rating.score = score
        rating.comments = comments
        flash("Rating updated.")

    else:
        
        db.session.add(Rating(temple_id=temple_id, score=score, user_id=user, comments=comments))
        flash("Rating added!")

    db.session.commit()
    

    return redirect("/temple/" + temple_id)
    #return redirect("/search/%s" % movie_id)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")