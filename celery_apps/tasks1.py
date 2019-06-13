from celery_apps import app
import time


@app.task
def add(x,y):
    print ("add",x,y)
    time.sleep(3)

    return x+y


