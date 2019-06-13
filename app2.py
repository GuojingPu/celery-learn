from tasks import fun2



if __name__ == '__main__':

    print ("开始执行函数")

    result = fun2.delay(5,5)
    result.ready()#执行完 true 未执行完false
    result.get() #获取执行结果

    print ("函数执行结束，结果：",result)