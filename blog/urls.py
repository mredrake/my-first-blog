from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import DinamicSitemap, StaticSitemap
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
robots_view = RedirectView.as_view(url='/robots.txt', permanent=True)


sitemaps = {'articles': DinamicSitemap, 'static': StaticSitemap}



urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),
   url(r'^favicon\.ico$', favicon_view, name='favicon'),
   url(r'^/static/robots\.txt$', robots_view, name='robots_redir'),
   url(r'^robots\.txt$', views.robots, name='robots'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
   url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
       name='django.contrib.sitemaps.views.sitemap')
]
