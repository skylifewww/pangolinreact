from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
     
    url(r'^(?P<slug>[_0-9a-zA-Z-]+)/$', 'content.views.page', name='page'),
     
     

)
