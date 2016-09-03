#from django.conf.urls.defaults import *
from django.conf.urls import url 
from blog.views import archive
"""
urlpatterns = patterns('', 
    url(r'^$', archive),
)
"""
urlpatterns = [ 
    url(r'^$', archive),
]
