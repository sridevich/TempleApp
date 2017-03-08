import requests
import json
from model import connect_to_db, db, Temple
from server import app

def getlatlong():

	temples = Temple.query.all()

	for temple in temples:
		
		if temple.zipcode = "OR" 
		address = temple.address + " " + temple.city + " " + temple.state + " " + temple.zipcode 
		print address
		#address = "683 Sutter Street, San Francisco, CA"


		r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=)
		adict = r.json()
		print adict

		lat = adict["results"][0]["geometry"]["location"]["lat"]
		lon = adict["results"][0]["geometry"]["location"]["lng"]


		temple.latitude = lat
		temple.longitude = lon

		db.session.commit()

		print lat, lon

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

47.686353
-122.133692
