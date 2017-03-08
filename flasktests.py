from unittest import TestCase
from server import app

class Flasktests(TestCase):
	def setUp(self):
		""" Stuff to do before every test. """

		self.client = app.test_client()
		app.config['TESTING'] = True


	def test_longin_flask_route(self):
		result = self.client.get("/")
		self.assertEqual(result.status_code, 200)
		self.assertIn(<h1> Search Temples in US </h1>, result.data)

	def test_login(self):
    	result = self.client.post("/login",
            data={"email": "ja@yahoo.com", "password": "Unknown8"},
                              follow_redirects=True)
    		self.assertIn("You are a valid user", result.data)

	def tearDown(Self):

class TempleDatabasetest(unittest.TestCase):
    """SQLAlchemy database test"""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        connect_to_db(app, "SQLAlchemy:///temples")
        app.config['SECRET_KEY'] = 'jgjjghhghvxffdrddtrtjjhjhjvvhghgggg'

    def tearDown(self):
        db.session.close()



