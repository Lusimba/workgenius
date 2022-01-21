import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mandrill_project.settings')


app = Celery('mandrill_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_data_1s': {
        'task': 'listener.tasks.get_mandrill_data',
        'schedule': 1.0
    }
}


app.autodiscover_tasks()