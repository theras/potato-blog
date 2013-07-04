import unittest
import datetime

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from ndbtestcase import NdbTestCase
from core.models import Post

from django.test.client import Client
from django.core.urlresolvers import reverse


class AdminTestCase(NdbTestCase):	
	def setUp(self):
		super(AdminTestCase, self).setUp()
		self.client = Client()

	def test_add_page(self):
		response = self.client.get(reverse('admin_add_post'))
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()