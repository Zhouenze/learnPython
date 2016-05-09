# -*- coding: utf-8 -*-             #中文注释需要

class myException(Exception):pass   #用户自定义异常要以类形式写（字符串已不行），触发实例对象，捕捉类对象；可选但最好继承自Exception
class myException2(myException):pass
try:
    var = 1                         #exception之前的代码已执行
    # raise IndexError              #发生没有被捕捉的异常则执行finally块然后异常向上传递，若传到默认异常处理会中断运行并打印信息（这里因为都被捕捉了所以不会发生）
    # raise WindowsError, 'infoHere'  #raise时可以附加数据，except后的异常名称后可以接收
    # raise myException()             #发生被捕捉的异常则执行异常代码、finally块然后继续
    raise myException2()            #只要except分句列举了异常的类或任何超类名则可匹配，所以这个会被myException匹配
    # assert 0, 'assertInfo'          #raise的定制版，可在发行时便捷去除
    var = 2                         #发生exception所以不执行
except myException:                 #下面三个都能捕捉myException但因为Python从上到下搜索相符except块所以这个优先
    print 'got my exception'
    # raise                         #单raise重新引发当前异常，常用于把刚捕捉的异常传递给另一个处理器或要捕捉但不希望它在此死掉时
except (myException, WindowsError, myException), info: #传入元组，三种异常同一块处理代码；搜索从左至右，但这没什么意义，右面的Exception是废代码但合法，info接收raise发来的额外信息
    print 'got one of two exceptions', info
except AssertionError, info:
    print 'got AssertionError', info
except:                             #任何未指定类型的异常由此捕捉，语法强制必须是最后一个except块（否则Python依次找符合的，后面的会被覆盖）
    print 'got some other exception'
else:                               #没发生异常的话在代码块后执行
    print 'else'
finally:                            #一定会执行，发生异常并被捕捉的话处理后执行，发生异常没被捕捉的话上传前执行，没异常的话else块后执行，即使处理过程中又发生异常也执行，基本用于清理
    print 'finally'
print 'continue ',var

class traceBlock:
    def message(self, arg):
        print 'running', arg
        return
    def __enter__(self):
        print 'starting with block'
        return self                 #如果with中有as则会获得该返回值，否则会忽略
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print 'exited normally' #正常退出时调用该函数，返回值无所谓
        else:
            print 'raise an exception', exc_type
            return True             #异常发生时调用该函数，如果返回False则异常重新引发，无本句则默认return None也是False
with traceBlock() as action:
    action.message('test1')
    print 'reach here'
with traceBlock() as action:
    action.message('test2')
    raise TypeError
    print 'can not reach here'

class myException3(Exception):pass
# raise myException3('string')
# raise myException3, myException3('string')    #2和4的区分：书上说如果raise语句中没有实例对象，Python就会创建实例
# raise myException3                            #raise myException3()
# raise myException3, 'string'                  #raise myException3('string')
# raise myException3, ('string1', 'string2')    #raise myException3('string1', 'string2')

try:
    1 / 0
except:
    import sys
    print sys.exc_info()    #如没发生过异常就返回三个None，如果有就是最近一次异常的(exceptionType, exceptionInstance, traceback)

try:
    import os
    # os._exit(1)           #os._exit(statuscode)是立即强制终止，什么都不干了
    sys.exit(2)             #sys.exit(statuscode)通过引发SystemExit异常来终止程序
except:pass                 #上面说的SystemExit被此处捕捉因此终止程序失败
print 'exit failed'

