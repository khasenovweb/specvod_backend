import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # 'check-transactions': {
    #     'task': 'main.tasks.check_transactions',
    #     'schedule': timedelta(seconds=10),
    # },
    # 'import_products': {
    #     'task': 'main.tasks.import_products',
    #     'schedule': timedelta(hours=1),
    # },
}