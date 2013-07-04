import unittest
import datetime

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from ndbtestcase import NdbTestCase
from core.models import Post

from django.test.client import Client
from django.core.urlresolvers import reverse

class PostTestCase(NdbTestCase):
	def setUp(self):
		super(PostTestCase, self).setUp()
		self.client = Client()

	def test_index_page(self):
		response = self.client.get(reverse('post_index'))
		self.assertEqual(response.status_code, 200)
	
	def test_archive_page(self):
		response = self.client.get(reverse('archive_index'))
		self.assertEqual(response.status_code, 200)
	
	def test_pass(self):
		pass

if __name__ == '__main__':
	unittest.main()