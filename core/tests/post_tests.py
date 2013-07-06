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
		self.post = Post(
			title = 'Test Post',
			brief = 'To infinity ... and beyond.',
			content = 'Vestibulum id ligula porta felis euismod semper.',
			is_active = True,
			comments_enabled = False,
			date_published = datetime.date(2013,07,04),
		)
		self.client = Client()

	def test_index_page(self):
		response = self.client.get(reverse('post_index'))
		self.assertEqual(response.status_code, 200)
	
	def test_archive_page(self):
		response = self.client.get(reverse('archive_index'))
		self.assertEqual(response.status_code, 200)
	
	def test_post_that_does_exist(self):
		self.post.put()
		response = self.client.get(reverse('post_view', args=[2013,07,04,'test-post']))
		self.assertEqual(response.status_code, 200)
	
	def test_post_that_does_not_exist(self):
		self.post.put()
		response = self.client.get(reverse('post_view', args=[2013,07,04,'i-dont-exist']))
		self.assertEqual(response.status_code, 404)
		
	def test_post_is_not_active(self):
		self.post.put()
		self.post.is_active = False
		self.post.put()
		response = self.client.get(reverse('post_view', args=[2013,07,04,'test-post']))
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.main()