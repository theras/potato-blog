from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Post, PostForm
from google.appengine.ext import ndb
from google.appengine.api import users
from django.http import Http404

import lib.markdown
import datetime

def post_index(request):
	user = users.get_current_user()
	posts = Post.query(Post.is_active == True).order(-Post.created_at)
	return render_to_response('post/index.html', RequestContext(request, locals()))

def post_view(request, slug, year, month, day):
	post = Post.query(
		ndb.AND(
			Post.slug == slug,
			Post.date_published == datetime.datetime(int(year), int(month), int(day)),
			Post.is_active == True,
		)
	).get()
	if post is None:
		raise Http404
	return render_to_response('post/view.html', RequestContext(request, locals()))

def archive_index(request):
	posts = Post.query(Post.is_active == True).order(-Post.created_at)
	return render_to_response('archive/index.html', RequestContext(request, locals()))