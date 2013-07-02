import unittest

from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from ndbtestcase import NdbTestCase
from core.models import Post
from core.views.admin_views import *
from django.test.client import RequestFactory


class AdminViewsTestCase(NdbTestCase):
	def test_add_post(self):
		post = Post(
			title = 'Test Post',
			brief = 'To infinity ... and beyond.',
			content = 'Vestibulum id ligula porta felis euismod semper.',
			is_active = True,
			comments_enabled = False,
		)
		post.put()
		post_key = ndb.Key(Post, 1)
		post_title = post_key.get().title
		
		self.assertEqual(post_title, post.title)
		
	def test_presence_of_add_post_page(self):
		self.factory = RequestFactory()
		request = self.factory.get('/admin/add/')
		response = admin_post_add(request)
		
		self.assertEqual(response.status_code, 200)
	
if __name__ == '__main__':
	unittest.main()

