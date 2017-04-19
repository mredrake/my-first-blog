from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import DinamicSitemap, StaticSitemap


sitemaps = {
    sitemaps = {'Post': sm.DinamicSitemap, 'static': sm.StaticSitemap}
}


urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
   url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
       name='django.contrib.sitemaps.views.sitemap')
]
