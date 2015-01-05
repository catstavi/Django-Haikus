from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poem_db.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^syllabize_db/', include('syllabize_db.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
