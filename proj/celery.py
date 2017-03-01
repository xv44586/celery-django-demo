# coding:utf-8
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from tasks import *
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动寻找每个app下的task.py
app.autodiscover_tasks()
# celery beat
"""
也可以写在Django的settings中
当前采用写在settings中
"""
'''
from datetime import timedelta
app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'add-every-6-seconds': {
            'task': 'proj.tasks.add',
            'schedule': timedelta(seconds=60),
            'args': (1, 2)
        },
        'multi-at-every-16-15-00':{
            'task':'proj.tasks.mul',
            'schedule': crontab(minute='35,36,37'),
            'args': (8, 9)
        }
    }
)
'''
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# app = Celery('proj',
#              broker='redis://localhost:6379/1',
#              backend='redis://localhost:6379/1',
#              include=['proj.tasks'])
# app.conf.update(
#     result_expires=3000
# )
# if __name__ == 'main':
#     app.start()
