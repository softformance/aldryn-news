# -*- coding: utf-8 -*-
from django.contrib import admin

from aldryn_news.forms import NewsForm
from aldryn_news.models import News

import cms
from cms.admin.placeholderadmin import PlaceholderAdmin
from distutils.version import LooseVersion
from hvad.admin import TranslatableAdmin


class NewsAdmin(TranslatableAdmin, PlaceholderAdmin):

    date_hierarchy = 'publication_start'
    list_display = ['__unicode__', 'publication_start', 'publication_end', 'all_translations']
    form = NewsForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {'fields': ['title', 'slug', 'publication_start', 'publication_end']}),
            (None, {'fields': ['key_visual', 'lead_in', 'tags']})
        ]

        # show placeholder field if not CMS 3.0
        if LooseVersion(cms.__version__) < LooseVersion('3.0'):
            fieldsets.append(
                ('Content', {
                    'classes': ['plugin-holder', 'plugin-holder-nopage'],
                    'fields': ['content']}))

        return fieldsets

admin.site.register(News, NewsAdmin)