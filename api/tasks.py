# coding:utf-8
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from proj.models import Person
from django.db.models import Q
import datetime

@shared_task
def check():
    # item = Person.objects.filter(content__contains=u'崩溃'）
    yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)
    checkitems = Person.objects.filter(Q(content__contains=u'崩溃') | Q(content__contains=u'漏洞') & Q(publish_time__gte=yesterday))
    checkitems = Person.objects.filter(Q(content__contains=u'崩溃') | Q(content__contains=u'漏洞')).exclude(\
        publish_time__lte=yesterday)

    itemslist = []
    for i in checkitems:
        # name = item[0].name'
        print i.publish_time
        itemslist.append(i.pk)
    return itemslist