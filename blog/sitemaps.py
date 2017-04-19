from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    
    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now())
    
    def lastmod(self, Post):
        return Post.published_date 

    def location(self, Post):
        return "/post/" + Post.pk + "/"
