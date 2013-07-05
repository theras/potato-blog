# Introduction

A Django-powered blog that runs on Google AppEngine.

* Uses [NDB](https://developers.google.com/appengine/docs/python/ndb/).
* Based on [Djappengine](https://github.com/potatolondon/djappengine/).
* Uses [Pagedown](https://code.google.com/p/pagedown/) as the Markdown editor.

# Demonstrations

Blog with posts:

[http://sraine-blog.appspot.com/](http://sraine-blog.appspot.com/)

Fresh blog:

[http://scott-blog-test.appspot.com/](http://scott-blog-test.appspot.com/)

# Installation

Make sure the Google AppEngine SDK is installed and you have created an application at [http://appengine.google.com](http://appengine.google.com).

####Clone the repository

`git clone git@bitbucket.org:luumina/potato-blog.git`

#### Install dependencies

`pip install -r requirements.txt`

#### Configuration

app.yaml

`application: your-app-name-here`

core/templates/posts/_disqus.html

`var disqus_shortname = 'your-disqus-shortname';`

core/templates/layout/base.html

`<title>YOUR BLOG NAME - {% block title %}{% endblock title %}</title>`

#### Tests

`./test.sh`

#### Serve Locally

`./serve.sh`

#### Deploy to AppEngine

`appcfg.py update .`