from celery_apps import tasks1
from celery_apps import tasks2


if __name__ == '__main__':

    print ("开始执行")
    tasks1. add.delay(2,3) #apply_async()
    tasks2.multiply.delay(2,3)

    print ('执行结束')

