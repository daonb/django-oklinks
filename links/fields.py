from django.contrib.contenttypes import generic
from models import Link

def LinksField(**kwargs):
    ''' use me to add a links field to your model '''
    return generic.GenericRelation(Link, content_type_field="content_type",
       object_id_field="object_pk")
