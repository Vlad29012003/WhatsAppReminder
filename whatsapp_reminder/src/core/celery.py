from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-reminders-every-minute': {
        'task': 'reminders.tasks.send_scheduled_reminders', 
        'schedule': 60.0,  
    },
}

app.conf.timezone = 'UTC'

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


