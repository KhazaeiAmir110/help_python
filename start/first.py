import time

from celery import Celery

app = Celery(main='tasks', broker='amqp://guest:guest@localhost:5672/')


@app.task(name='first.adding')
def add(a, b):
    time.sleep(20)
    return a + b


# add.delay(1,2)
# add.apply_async(args=[1, 2], queue='first.adding', countdown=10, expires=30)


@app.task(bind=True, name='first.division')
def division(self, a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Sorry, division by zero")
        self.retry()