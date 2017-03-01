
# coding:utf-8
from __future__ import absolute_import, unicode_literals
from .models import Person

def get(request):
    p = Person.objects.all()
    for pi in p:
        print pi.name
    item = Person.objects.filer(content_contains=u'崩溃')
    print item.name
    name = item.name
    return name