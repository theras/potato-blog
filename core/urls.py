from django.conf.urls.defaults import *
from django.conf import settings
from core import views

urlpatterns = patterns('core.views',
    url(
        r'^$',
        'post_index',
        name = 'post_index',
    ),
    
    url(
        r'^admin/$',
        'admin_post_list',
        name = 'admin_post_list',
    ),
    
    url(
        r'^post/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/edit/$',
        'admin_post_edit',
        name = 'admin_post_edit',
    ),
    
    url(
        r'^post/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/delete/$',
        'admin_post_delete',
        name = 'admin_post_delete',
    ),
    
    url(
        r'^post/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        'post_view', 
        name = 'post_view',
    ),
    
    url(
        r'^admin/add/$',
        'admin_post_add',
        name = 'admin_post_add',
    ),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        )