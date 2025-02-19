from celery import Celery

app = Celery('periodic', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')

app.config_from_object("celery_config")


@app.task
def show(name):
    print(f"Hellow {name}")
