import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_practica.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CElERY')
app.autodiscover_tasks()