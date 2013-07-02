import unittest

from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from ndbtestcase import NdbTestCase

from core.models import Post


class AdminViewsTestCase(NdbTestCase):
	def testAddPost(self):
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
	
if __name__ == '__main__':
	unittest.main()

