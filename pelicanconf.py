#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jay Heselberth'
SITENAME = u'Hesselberth Lab'
SITEURL = 'http://hesselberthlab.github.io'

PATH = 'content'

THEME = 'themes/pelican-bootstrap3'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'
GOOGLE_ANALYTICS='UA-54095998-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jayhesselberth'),
          ('github', 'http://github.com/hesselberthlab'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
