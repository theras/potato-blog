from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Post, PostForm
from google.appengine.ext import ndb

import lib.markdown
import datetime

def post_index(request):
	posts = Post.query(Post.is_active == True).order(-Post.created_at)
	return render_to_response('post/index.html', RequestContext(request, locals()))

def post_view(request, slug, year, month, day):
	post = Post.query(
		ndb.AND(
			Post.slug == slug,
			Post.date_published == datetime.datetime(int(year), int(month), int(day))
		)
	).get()
	return render_to_response('post/view.html', RequestContext(request, locals()))

def archive_index(request):
	posts = Post.query(Post.is_active == True).order(-Post.created_at)
	return render_to_response('archive/index.html', RequestContext(request, locals()))