# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from aldryn_news.views import ArchiveView, NewsDetailView, TaggedListView
from aldryn_news.feeds import LatestEntriesFeed, TagFeed

urlpatterns = patterns(
    '',
    url(r'^$', ArchiveView.as_view(), name='latest-news'),
    url(r'^feed/$', LatestEntriesFeed(), name='latest-news-feed'),
    url(r'^(?P<year>\d{4})/$', ArchiveView.as_view(), name='archive-year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', ArchiveView.as_view(), name='archive-month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$', NewsDetailView.as_view(), name='news-detail'),
    url(r'^tagged/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='tagged-posts'),
    url(r'^tagged/(?P<tag>[-\w]+)/feed/$', TagFeed(), name='tagged-news-feed'),
)