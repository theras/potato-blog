from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Post, PostForm
from google.appengine.ext import ndb

import datetime

def admin_add_post(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = Post(
				title = form.cleaned_data['title'],
				brief = form.cleaned_data['brief'],
				content = form.cleaned_data['content'],
				is_active = form.cleaned_data['is_active'],
				comments_enabled = form.cleaned_data['comments_enabled'],
			)
			post.put()
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form = PostForm()
	return render_to_response('admin/add.html', RequestContext(request, locals()))

def admin_edit_post(request, slug, year, month, day):
	post = Post.query(ndb.AND(Post.slug == slug, Post.date_published == datetime.datetime(int(year), int(month), int(day)))).get()
	form = PostForm(initial = post.to_dict())
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post.title = form.cleaned_data['title']
			post.brief = form.cleaned_data['brief']
			post.content = form.cleaned_data['content']
			post.is_active = form.cleaned_data['is_active']
			post.comments_enabled = form.cleaned_data['comments_enabled']
			post.put()
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form
	return render_to_response('admin/edit.html', RequestContext(request, locals()))

def admin_delete_post(request, slug, year, month, day):
	post = Post.query(ndb.AND(Post.slug == slug, Post.date_published == datetime.datetime(int(year), int(month), int(day)))).get()
	post.key.delete()
	return HttpResponseRedirect('/')