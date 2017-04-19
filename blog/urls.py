from django.conf.urls import url
from . import views
from django.contrib.sitemaps import views


urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
   url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
   url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
