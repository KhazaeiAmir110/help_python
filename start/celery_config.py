from celery.schedules import crontab

broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

beat_schedules = {
    "call_show_every_minute": {
        "task": "periodic.show",
        "schedule": crontab(minute="*/1"),
        "args": ("amir", )
    }
}
