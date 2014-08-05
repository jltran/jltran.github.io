#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jason L. Tran'
SITENAME = u'Jason Tran//jason.lt'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = "bootstraped"

# Articles all receieve a relative URL
ARTICLE_URL = '/{date:%Y}/{slug}/'

# Bootstraped variable; customize size of char. shown on main page.
DEFAULT_TRUNCATE = 500
NON_GENERIC_BOOTSTRAP = "cosmo"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/jltran'),
          ('Twitter', 'https://twitter.com/zjodak'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
	'extra/CNAME': {'path': 'CNAME'},
}
