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
		post = new_post.put().get()
		response = self.client.get(reverse('post_view', args=[
			post.date_published.strftime("%Y"),
			post.date_published.strftime("%m"),
			post.date_published.strftime("%d"),
			slugify(post.title)])
		)
		self.assertEqual(response.status_code, 200)
	
	def test_if_edit_page_is_reachable(self):
		post = self.post.put().get()
		response = self.client.get(
			reverse('admin_edit_post', args=[
				post.date_published.strftime("%Y"),
				post.date_published.strftime("%m"),
				post.date_published.strftime("%d"),
				slugify(post.title)])
		)
		self.assertEqual(response.status_code, 200)
		
	def test_edit_exisiting_post(self):
		post = self.post.put().get()
		post.title = 'Cool New Title'
		edited_post = post.put().get()
		response = self.client.get(
			reverse('admin_edit_post', args=[
			edited_post.date_published.strftime("%Y"),
			edited_post.date_published.strftime("%m"),
			edited_post.date_published.strftime("%d"),
			slugify(edited_post.title)])
		)
		self.assertEqual(response.status_code, 200)
	
	def test_delete_method(self):
		deleted_post = self.post.put().delete()
		self.assertEqual(deleted_post, None)
		

if __name__ == '__main__':
	unittest.main()