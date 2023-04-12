import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metaatafrica.settings")

app = Celery("metaatafrica")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.timezone = 'Africa/Lagos'

#   app.conf.beat_schedule = {
#       'run-me-every-minute':
#           {
#               'task': 'tasks.get_data_every_minute',
#               'schedule': crontab(minute=1),
#           }
#   }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
