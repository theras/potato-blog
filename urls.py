from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^appengine_sessions/',
        include('appengine_sessions.urls')
    ),
    
    url(
        r'',
        include('core.urls')
    ),
)
