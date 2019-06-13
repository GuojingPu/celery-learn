from celery import Celery
import time
app = Celery('tasks_1',broker='redis://127.0.0.1:6379/0',backend='redis://127.0.0.1:6379/1')


@app.task
def fun(x,y):
    print ("执行耗时函数fun")

    time.sleep(3)

    return x+y



@app.task
def fun2(x,y):
    print ("执行耗时函数fun2")

    time.sleep(3)

    return x*y


if __name__ == '__main__':

    ##直接在tasks中调用会报错,在其他文件中导入使用
    print ("开始执行函数")

    result = fun.delay(3,5)

    print ("函数执行结束，结果：",result)
