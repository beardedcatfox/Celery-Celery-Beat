import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-new-quotes-every-2-hours': {
        'task': 'cel.task.fetch_new_quotes',
        'schedule': crontab(minute=0, hour='1-23/2')
    },
}
