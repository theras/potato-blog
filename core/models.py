from google.appengine.ext import ndb
from django import forms
from django.template.defaultfilters import slugify
import datetime

class Post(ndb.Model):
	title = ndb.StringProperty()
	date_published = ndb.DateProperty(auto_now_add = True)
	created_at = ndb.DateTimeProperty(auto_now_add = True)
	brief = ndb.StringProperty()
	content = ndb.TextProperty()
	is_active = ndb.BooleanProperty(default = True)
	slug = ndb.ComputedProperty(lambda self: slugify(self.title))
	comments_enabled = ndb.BooleanProperty(default = True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/post/%i/%s/%s/%s/' % (
			self.date_published.year,
			self.date_published.strftime("%m"),
			self.date_published.strftime("%d"),
			self.slug,
		)

	def get_edit_url(self):
		return '/admin/%i/%s/%s/%s/edit/' % (
			self.date_published.year,
			self.date_published.strftime("%m"),
			self.date_published.strftime("%d"),
			self.slug,
		)

	def get_delete_url(self):
		return '/admin/%i/%s/%s/%s/delete/' % (
			self.date_published.year,
			self.date_published.strftime("%m"),
			self.date_published.strftime("%d"),
			self.slug,
		)

class PostForm(forms.Form):
	title = forms.CharField()
	brief = forms.CharField()
	content = forms.CharField(widget = forms.Textarea, help_text='This field supports markdown')
	is_active = forms.BooleanField(required = False, label = 'Visible to public?')
	comments_enabled = forms.BooleanField(required = False, label = 'Enable comments?')