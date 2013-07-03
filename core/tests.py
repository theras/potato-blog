import unittest
import datetime

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from ndbtestcase import NdbTestCase
from core.models import Post
from core.views.admin_views import *
from django.test.client import RequestFactory


class CoreTestCase(NdbTestCase):	
	def setUp(self):
		super(CoreTestCase, self).setUp()
		self.post = Post(
			title = 'Test Post',
			brief = 'To infinity ... and beyond.',
			content = 'Vestibulum id ligula porta felis euismod semper.',
			is_active = True,
			comments_enabled = False,
		)
		self.post.put()
		self.post_key = ndb.Key(Post, 1)
		self.post = self.post_key.get()
	
	def test_post_exists(self):
		self.factory = RequestFactory()
		request = self.factory.get(self.post.get_absolute_url())
		response = admin_post_edit(
			request,
			# App Engine throws an error when using self.post.slug :/
			# Most likely because there is no SlugProperty?
			'test-post',
			self.post.date_published.year,
			self.post.date_published.strftime("%m"),
			self.post.date_published.strftime("%d"),
		)
		self.assertEqual(response.status_code, 200)

	def test_add_post(self):
		post_title = self.post.title
		self.assertEqual(post_title, self.post.title)

	def test_add_post_exists(self):
		self.factory = RequestFactory()
		request = self.factory.get('/admin/add/')
		response = admin_post_add(request)
		self.assertEqual(response.status_code, 200)

	def test_edit_post(self):
		self.post.title = 'Updated Post'
		self.post.put()
		self.assertEqual(self.post.title, ndb.Key(Post, 1).get().title)

	def test_edit_post_exists(self):
		self.factory = RequestFactory()
		request = self.factory.get(self.post.get_edit_url())
		response = admin_post_edit(
			request,
			# App Engine throws an error when using self.post.slug :/
			# Most likely because there is no SlugProperty?
			'test-post',
			self.post.date_published.year,
			self.post.date_published.strftime("%m"),
			self.post.date_published.strftime("%d"),
		)
		self.assertEqual(response.status_code, 200)

	def test_delete_post(self):
		self.post_key.delete()
		self.assertEqual(self.post_key.get(), None)

if __name__ == '__main__':
	unittest.main()
