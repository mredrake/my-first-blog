from django.conf.urls import url
from . import views
from django.contrib.sitemaps import views as stmpviews


urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
   url(r'^sitemap\.xml$', stmpviews.index, {'sitemaps': sitemaps}),
   url(r'^sitemap-(?P<section>.+)\.xml$', stmpviews.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
