# Development settings for {{ project_name }}
from config.defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Change this to work with your default development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                       # Or path to database file if using sqlite3.
        'USER': '',                       # Not used with sqlite3.
        'PASSWORD': '',                   # Not used with sqlite3.
        'HOST': '',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                       # Set to empty string for default. Not used with sqlite3.
    }
}

# Attempt to load any settings from config.local_development, but ignore any
# errors complaining about them not being present.
try:
    from config.local_development import *
except ImportError, e:
    pass
