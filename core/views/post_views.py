from django.shortcuts import render
from core.models import Post, PostForm
from google.appengine.ext import ndb
from google.appengine.api import users
from django.http import Http404

import lib.markdown
import datetime

def post_index(request):
	posts = Post.query(Post.is_active == True).order(-Post.created_at).fetch()
	
	r = render(
		request, 'post/index.html',
		{ 'posts': posts }
	)
	return r

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
		
	r = render(
		request, 'post/view.html',
		{ 'post': post }
	)
	return r

def archive_index(request):
	posts = Post.query(Post.is_active == True).order(-Post.created_at).fetch()
	
	r = render(
		request, 'archive/index.html',
		{ 'posts': posts }
	)
	return r