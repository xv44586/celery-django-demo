# coding:utf-8
from __future__ import absolute_import,unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Person(models.Model):

    sex = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    publish_time = models.DateTimeField(default=datetime.datetime.now, blank=True)

    class Meta:
        db_table = 'Person'
