import server
import unittest
from unittest import TestCase
from server import app


class TempleAppIntegrationTestCase(unittest.TestCase):
	def setUp(self):
		""" Stuff to do before every test. """

		self.client = server.app.test_client()
		server.app.config['TESTING'] = True

	def test_index(self):

		result = client.get('/')
		self.assertIn('<h1> Search Temples in US </h1>', result.data)

	def test_login(self):
		client = server.app.test_client()
    	result = client.post("/login",
            data={"email": "ja@yahoo.com", "password": "Unknown8"},
                              follow_redirects=True)
    		self.assertIn("Login", result.data)

	def tearDown(Self):

# class TempleDatabasetest(unittest.TestCase):
#     """SQLAlchemy database test"""

#     def setUp(self):
#         self.client = app.test_client()
#         app.config['TESTING'] = True
#         connect_to_db(app, "SQLAlchemy:///templestest")
#         app.config['SECRET_KEY'] = 'jgjjghhghvxffdrddtrtjjhjhjvvhghgggg'

#     def tearDown(self):
#         db.session.close()


# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		