from celery_apps import app
import time

@app.task
def multiply(x,y):
    print ("multiply",x,y)
    time.sleep(3)

    return x*y