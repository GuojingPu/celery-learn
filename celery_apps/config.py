

BROKER_URL = 'redis://127.0.0.1:6379/0'

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'

CELERY_TIMEZONE = 'Asia/Shanghai'


#导入指定的任务模块
CELERY_IMPORTS = (
    'celery_apps.tasks1',
    'celery_apps.tasks2',
)
