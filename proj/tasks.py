from __future__ import absolute_import,unicode_literals

from proj.celery import app
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@app.task
def xsum(number):
    return sum(number)

@shared_task
def mul(x, y):
    return x * y

