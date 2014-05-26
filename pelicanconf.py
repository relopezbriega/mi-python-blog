#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raul E. Lopez Briega'
SITENAME = u'Raul E. Lopez Briega'
SITESUBTITLE = u'Mi blog personal sobre python'
SITEURL = ''

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MENUITEMS = [('About', '/pages/acerca-de-mi.html'),
             ('Home Page', '/index.html'),             
             ('Archives', '/archives.html')]

# Blogroll
LINKS =  (('Mi otro blog', 'http://relopezbriega.com.ar'),
		  ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-octopress-theme/'

DISPLAY_PAGES_ON_MENU = False

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

STATIC_PATHS = ['images', 'figures', 'downloads', 'pages', 'favicon.png']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sharing
TWITTER_USER = 'relopezbriega'
GOOGLE_PLUS_USER = 'relopezbriega'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True
