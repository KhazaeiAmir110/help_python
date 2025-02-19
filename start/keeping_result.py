from celery import Celery

app = Celery('keep-result', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')


@app.task(name="keep")
def full_name(name, family):
    return f'This is FullName : {name} {family}'
