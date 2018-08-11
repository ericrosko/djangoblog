#!/usr/bin/env python

"""
Lesson 8 requirement
"""

from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post
from myblog.models import Category

class LatestEntriesFeed(Feed):
    title = "Django Blog Posts"
    link = "/latest/feed"
    description = "Updates on the posts on djangoblog project lesson 8"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse('posts', args=[item.pk])
