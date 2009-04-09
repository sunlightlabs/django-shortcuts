# django-secretballot

Django shortcut application that allows redirects to be created from the Django admin app.

django-shortcuts is a project of Sunlight Labs (c) 2009.
Written by Jeremy Carbaugh <jcarbaugh@sunlightfoundation.com>

Source: http://github.com/sunlightlabs/django-shortcuts/


## Requirements

python >= 2.4

django >= 1.0


## Installation

To install run 

	python setup.py install

which will install the application into the site-packages directory.

## Usage


### settings.py

To enable django-shortcuts, add _shortcuts_ to INSTALLED_APPS.

By default, all aliases will be served from:

	http://[configured_url]/s/[alias]

The _p_ prefix can be changed by setting __SHORTCUT_PREFIX__ in settings.py.


### urls.py

Add a reference to _shortcut.urls_. For example:

	url(r'^', include('shortcuts.urls')),
