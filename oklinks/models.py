import os

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from managers import LinksManager, LinkTypeManager

class LinkType(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    image = models.ImageField(upload_to='icons')

    objects = LinkTypeManager()

    class Meta:
        verbose_name = _('link type')
        verbose_name_plural = _('link types')

    def __unicode__(self):
        return self.title

class Link(models.Model):
    url = models.URLField(verbose_name='URL', max_length=1000,
                          verify_exists=False)
    title = models.CharField(max_length=200, verbose_name=_('title'))
    content_type   = models.ForeignKey(ContentType,
            verbose_name=_('content type'),
            related_name="content_type_set_for_%(class)s")
    object_pk      = models.TextField(_('object ID'))
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    link_type = models.ForeignKey(LinkType, default=LinkTypeManager.default)
    active = models.BooleanField(default=True)
    objects = LinksManager()

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')

    def __unicode__(self):
        return "%s: %s" % (self.title, self.url)

class LinkedFile(models.Model):
    link = models.ForeignKey(Link, null=True, blank=True, default=None)
    sha1 = models.CharField(max_length=1000, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    link_file = models.FileField(upload_to='link_files')
