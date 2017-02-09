"""Models and database functions for Temple App project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()
###########################################################################################
""" Model definitions """

class User(db.Model):
    """ User of the Temple App """

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(60), nullable=False)
    pass_word = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(60), nullable=True)
    last_name = db.Column(db.String(60), nullable=True)
    age = db.Column(db.Integer, nullable=True)

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<(User user_id=%s email=%s pass_word=%s>"
                "<first_name=%s last_name=%s age=%s)>") % (self.user_id, 
                                        self.email, self.pass_word, 
                                        self.first_name, self.last_name, 
                                        self.age)

class Temple(db.Model):
    """ Class object for the Temple table"""


    __tablename__ = "temples"

    temple_id = db.Column(db.String(5), primary_key=True)
    t_name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.String(15),nullable=False)
    email=db.Column(db.String(60), nullable=True)
    longitude=db.Column(db.Integer, nullable=True)
    latitude=db.Column(db.Integer, nullable=True)


    def _repr__(self):
        return ("<Temple temple_id=%s t_name=%s address=%s city=%s>"
                "<state=%s zipcode=%s email=%s longitude=%s latitude=%s >") % (self.temple_id, 
                                            self.t_name, self.address, self.city, self.state,
                                            self.zipcode, self.email, self.longitude, 
                                            self.latitude)

class Rating(db.Model):
    """ Class object for the Ratings table."""
    
    __tablename__="ratings"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    temple_id = db.Column(db.String(5), db.ForeignKey('temples.temple_id'))
    score = db.Column(db.Integer)
    comments = db.Column(db.String(300), nullable=True)

    
    user = db.relationship("User",
                           backref=db.backref("ratings", order_by=rating_id))

    temple = db.relationship("Temple",
                           backref=db.backref("ratings", order_by=rating_id))

    def __repr__(self):
        return ("<Rating rating_id=%s user_id=%s temple_id=%s>"
               "<score=%s comments=%s>") % (self.rating_id, 
                                            self.user_id, 
                                            self.temple_id, 
                                            self.score, self.comments)

class Phone(db.Model):
    "Class object for table phone"

    __tablename__ = "phones"

    phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_no_1 = db.Column(db.String)
    phone_no_2 =db.Column(db.String)
    temple_id = db.Column(db.String(5), db.ForeignKey('temples.temple_id'))

    temple = db.relationship("Temple",
                             backref=db.backref("phones")

    def __repr__(self):
        return "<Phone phone_id=%s phone_no=%s temple_id=%s>" % (self.phone_id, 
                                                                self.phone_no,
                                                                self.temple_id)

class Savesearch(db.Model):
    """Class object for the usersaves table"""

    __tablename__="savesearches"

    saveid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    temple_id=db.Column(db.String(5), db.ForeignKey('temples.temple_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship("User", backref=db.backref("savesearches")

    def __repr__(self):
        return "<Savesearch temple_id=%s user_id=%s" % (self.temple_id, self.user_id)
#####################################################################################################

# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""
    
    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///temples'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
    