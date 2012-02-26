from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

class LinkTypeManager(models.Manager):
    _default_linktype = False

    @property
    def default(self):
        if not self._default_linktype:
            self._default_linktype = self.get(title='default')
        return self._default_linktype

class LinksManager(models.Manager):

    def for_model(self, model):
        """
        QuerySet for all links for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_query_set().filter(content_type=ct)
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_unicode(model._get_pk_val()))
        return qs
