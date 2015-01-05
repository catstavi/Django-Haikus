from django.conf.urls import patterns, url

from syllabize_db import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
