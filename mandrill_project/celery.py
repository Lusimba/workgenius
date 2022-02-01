import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mandrill_project.settings')

# instatiating the Celery class as app
app = Celery('mandrill_project')

# Specify a prefix for Celery configuration in the settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')


# Configure the scheduler with the celery beat scheduler
app.conf.beat_schedule = {
    'get_data_1s': {
        'task': 'listener.tasks.get_mandrill_data',
        'schedule': 1.0
    }
}


app.autodiscover_tasks()