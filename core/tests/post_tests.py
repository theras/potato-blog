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
		post = self.post.put().get()
		response = self.client.get(reverse('post_view', args=[
			post.date_published.strftime("%Y"),
			post.date_published.strftime("%m"),
			post.date_published.strftime("%d"),
			slugify(post.title)])
		)
		self.assertEqual(response.status_code, 200)
	
	def test_post_that_does_not_exist(self):
		new_title = 'I don\'t exist'
		post = self.post.put().get()
		response = self.client.get(reverse('post_view', args=[
			post.date_published.strftime("%Y"),
			post.date_published.strftime("%m"),
			post.date_published.strftime("%d"),
			slugify(new_title)])
		)
		self.assertEqual(response.status_code, 404)
		
	def test_post_is_not_active(self):
		post = self.post.put().get()
		post.is_active = False
		edited_post = post.put().get()
		response = self.client.get(reverse('post_view', args=[
			edited_post.date_published.strftime("%Y"),
			edited_post.date_published.strftime("%m"),
			edited_post.date_published.strftime("%d"),
			slugify(edited_post.title)])
		)
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.main()