#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jay Heselberth'
SITENAME = u'Hesselberth Lab'
GITHUB_USER = 'hesselberthlab'
SITEURL = 'http://hesselberthlab.github.io'

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

PDF_GENERATOR = True

MENUITEMS = (
    ('People', '/pages/people.html'),
    ('Projects', '/pages/projects.html'),
    ('Publications', '/pages/publications.html'),
    ('Resources', '/pages/resources.html'),
    ('Contact', '/pages/contact.html'),
                    )
PATH = 'content'

THEME = 'hesselberth-theme'

BOOTSTRAP_THEME = 'lavish'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'
GOOGLE_ANALYTICS='UA-54095998-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Faculty web page',
          'http://www.ucdenver.edu/academics/colleges/medicalschool/departments/biochemistry/Faculty/PrimaryFaculty/Pages/Hesselberth.aspx'),
         ('Genome Informatics Workshop','http://hesselberthlab.github.io/workshop'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jayhesselberth'),
          ('github', 'http://github.com/hesselberthlab'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
