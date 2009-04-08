from django.conf import settings
from django.conf.urls.defaults import *

SHORTCUT_PREFIX = getattr(settings, "SHORTCUT_PREFIX", "s")

urlpatterns = patterns('',
    url(r'^%s/(?P<alias>\w+)/' % SHORTCUT_PREFIX, 'shortcuts.views.redirect', name="shortcut_redirect"),
)