AUTHOR = 'Henry'
SITENAME = 'Royal City Suds'
SITEURL = ""

PATH = "content"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

THEME = 'themes/flex'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


SHOW_SIDEBAR = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
