from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import logging
logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Ho_Chi_Minh')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'copy_report_24hrs': {
        'task': 'app.tasks.copy_report_24hrs',
        'schedule': crontab(hour=0, minute=0),
        # 'schedule': timedelta(seconds=5),
    }
    
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))