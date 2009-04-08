from django.db import models

class Shortcut(models.Model):
    alias = models.CharField(max_length=32)
    redirect = models.URLField(verify_exists=False)
    interval = models.PositiveIntegerField(default=1)
    title = models.CharField(blank=True, null=True)
    analytics = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s -> %s" % (self.alias, self.redirect)

    def uses_analytics(self):
        return not self.analytics is None