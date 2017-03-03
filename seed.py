"""Utility file to seed temples database from a csv file/"""

from sqlalchemy import func

from model import User, Temple, Rating, Phone, Savesearch, connect_to_db, db
from server import app

test1 = open("seed_data/templedata.txt")
print test1

def load_templedata():
    """Load temple information from  templedata into database."""
    
    for row in open("seed_data/templedata.txt"):
        #print row
    
        row = row.rstrip()   
        #print row
        #print row.split("\t")
        temple_id, t_name, address, city, state, zipcode = row.split("\t")


        temples = Temple(temple_id=temple_id,
                         t_name = t_name,
                         address = address,
                         city = city,
                         state = state,
                         zipcode = zipcode
                         )
        db.session.add(temples)

    db.session.commit()


def load_users():
    """ loads user information from a file"""

    for row in open("seed_data/userinfo.txt"):
        print row

        row = row.rstrip()

        email, pass_word, first_name, last_name, address, city, state = row.split(",")

        users = User(email=email, 
                pass_word=pass_word,
                first_name=first_name,
                last_name=last_name, 
                address=address, 
                city=city, 
                state=state)
        db.session.add(users)

    db.session.commit()
test1 = open("seed_data/phonedata.txt")
#print test1
def load_phones():
    """ loads phones numbers of temples from a file. """

    for row in open("seed_data/phonedata.txt"):
        print row

        row = row.rstrip()

        #phone_no_1, nothing, temple_id = row.split("\t")
        phonelist = row.split("\t")

        phone_no_1 = phonelist[0]
        temple_id = phonelist[2]

        #print len(listtest)
        phones = Phone(phone_no_1=phone_no_1,
                        temple_id=temple_id)

        db.session.add(phones)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_templedata()
    load_users()
    load_phones()
    