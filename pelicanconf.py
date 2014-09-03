#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jay Hesselberth'
SITENAME = u'Hesselberth Lab'
GITHUB_USER = 'hesselberthlab'
SITEURL = 'http://hesselberthlab.github.io'

DEFAULT_DATE = 'fs'

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

BOOTSTRAP_NAVBAR_INVERSE = False

PDF_GENERATOR = True

MENUITEMS = (
    ('People <span class="fa fa-group"></span>', '/pages/people.html'),
    ('Projects <span class="fa fa-coffee"></span>', '/pages/projects.html'),
    ('Publications <span class="fa fa-book"></span>', '/pages/publications.html'),
    ('Resources <span class="fa fa-archive"></span>', '/pages/resources.html'),
    ('Contact <span class="fa fa-envelope"></span>', '/pages/contact.html'),)

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'pelican_fontawesome',
    'better_figures_and_images',]

PATH = 'content'

THEME = 'hesselberth-theme'

BOOTSTRAP_THEME = 'yeti_zissou'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'
GOOGLE_ANALYTICS='UA-54095998-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ( ('Genome Informatics Workshop','http://hesselberthlab.github.io/workshop'),
          ('University Webpage',
          'http://www.ucdenver.edu/academics/colleges/medicalschool/departments/biochemistry/Faculty/PrimaryFaculty/Pages/Hesselberth.aspx'),)
         
# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jayhesselberth'),
          ('github', 'http://github.com/hesselberthlab'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
