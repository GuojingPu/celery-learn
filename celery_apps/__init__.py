from celery import Celery

app = Celery('my_tasks')

app.config_from_object("celery_apps.config")
