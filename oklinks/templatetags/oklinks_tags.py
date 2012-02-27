from django import template
from oklinks.models import Link
from django.conf import settings

register = template.Library()

# TODO: move _object_links to include/object_links.html
@register.inclusion_tag('oklinks/_object_links.html')
def object_links(object):
    l = Link.objects.for_model(object)
    return {'links': l, 'MEDIA_URL': settings.MEDIA_URL}

