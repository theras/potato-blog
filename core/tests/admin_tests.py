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
		self.post = Post(
			title = 'Test Post',
			brief = 'To infinity ... and beyond.',
			content = 'Vestibulum id ligula porta felis euismod semper.',
			is_active = True,
			comments_enabled = False,
			date_published = datetime.date(2013,07,04),
		)
		self.client = Client()

	def test_add_page(self):
		# Is the add page reachable
		response = self.client.get(reverse('admin_add_post'))
		self.assertEqual(response.status_code, 200)
		
		# Add a new post and check it is reachable
		new_post = Post(
			title = 'I Am New',
			brief = 'The Good, The Bad, and The Ugly.',
			content = 'Cras justo odio, dapibus ac facilisis in, egestas eget quam.',
			is_active = True,
			comments_enabled = False,
			date_published = datetime.date(2012,11,22),
		)
		new_post.put()
		response = self.client.get(reverse('post_view', args=[2012,11,22,'i-am-new']))
		self.assertEqual(response.status_code, 200)
	
	def test_edit_page(self):
		# Insert initial post
		self.post.put()
		
		# Is the edit page for a post reachable
		response = self.client.get(
			reverse('admin_edit_post', 
			args=[2013,07,04,'test-post'])
		)
		self.assertEqual(response.status_code, 200)
		
		# Edit exisitng post and check it updates
		self.post.title = 'Cool New Title'
		self.post.put()
		response = self.client.get(
			reverse('post_view', 
			args=[2013,07,04,'cool-new-title'])
		)
		self.assertEqual(response.status_code, 200)
	
	def test_delete_method(self):
		# Insert initial post
		self.post.put()
		
		# Delete post and make sure it returns 404
		self.post.key.delete()
		response = self.client.get(
			reverse('post_view', 
			args=[2013,07,04,'test-post'])
		)
		self.assertEqual(response.status_code, 404)
		

if __name__ == '__main__':
	unittest.main()