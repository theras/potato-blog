import unittest
import datetime

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from ndbtestcase import NdbTestCase
from core.models import Post

from django.test.client import Client
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


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

	def test_if_add_page_is_reachable(self):
		response = self.client.get(reverse('admin_add_post'))
		self.assertEqual(response.status_code, 200)
		
	def test_add_new_post(self):
		new_post = Post(
			title = 'I Am New',
			brief = 'The Good, The Bad, and The Ugly.',
			content = 'Cras justo odio, dapibus ac facilisis in, egestas eget quam.',
			is_active = True,
			comments_enabled = False,
			date_published = datetime.date(2012,11,22),
		)
		new_post.put()
		response = self.client.get(reverse('post_view', args=[
			new_post.date_published.strftime("%Y"),
			new_post.date_published.strftime("%m"),
			new_post.date_published.strftime("%d"),
			slugify(new_post.title)])
		)
		self.assertEqual(response.status_code, 200)
	
	def test_if_edit_page_is_reachable(self):
		self.post.put()
		response = self.client.get(
			reverse('admin_edit_post', args=[
				self.post.date_published.strftime("%Y"),
				self.post.date_published.strftime("%m"),
				self.post.date_published.strftime("%d"),
				slugify(self.post.title)])
		)
		self.assertEqual(response.status_code, 200)
		
	def test_edit_exisiting_post(self):
		self.post.put()
		self.post.title = 'Cool New Title'
		self.post.put()
		response = self.client.get(
			reverse('admin_edit_post', args=[
			self.post.date_published.strftime("%Y"),
			self.post.date_published.strftime("%m"),
			self.post.date_published.strftime("%d"),
			slugify(self.post.title)])
		)
		self.assertEqual(response.status_code, 200)
	
	def test_delete_method(self):
		# Test method not correct, too fix.
		pass
		

if __name__ == '__main__':
	unittest.main()