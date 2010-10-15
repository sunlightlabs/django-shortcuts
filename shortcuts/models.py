from django.db import models

METHODS = (
    ('http301', 'HTTP 301 (permanent)'),
    ('http302', 'HTTP 302 (temporary)'),
    ('htmlmeta', 'HTML meta (allows analytics)'),
)

class Shortcut(models.Model):
    alias = models.CharField(max_length=32, unique=True)
    redirect_to = models.URLField(verify_exists=False)
    method = models.CharField(max_length=8, default='http301', choices=METHODS)
    interval = models.PositiveSmallIntegerField(default=0, help_text="Number of seconds until redirect occurs. Defaults to 0 (instant).")
    title = models.CharField(max_length=128, blank=True)
    analytics = models.TextField(blank=True)
    
    def __unicode__(self):
        return u"%s -> %s" % (self.alias, self.redirect_to)