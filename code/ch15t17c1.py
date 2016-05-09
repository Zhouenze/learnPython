# -*- coding: utf-8 -*-             #中文注释需要

X = 99
L = []
def func():
    L.append(5)     #虽然改变了但不是赋值语句，L仍是全局变量不是本地变量
    print L         #全局版本
    # L = 1         #解注释会和上面冲突：有赋值语句的话L在整个本地命名空间都是本地变量，和上面的全局变量用法冲突
    # print X       #解注释会和下面冲突：X由下面已确定是本地变量，还没产生就引用。这里无法引用到全局版本
    X = 98          #X是本地变量与外界不冲突
    print X         #本地版本
    global Z        #不管是否有赋值语句，Z认为是全局变量
    Z = 100         #原来没有，在全局新创建了
    return
func()
print L, X, Z       #全局版本

def func2():
    print 3         #没有return自动返回None
func3 = func2       #函数也是对象，可以多名引用
def func4(func):    #函数也是对象，可以参数传递
    func()
    return
func3()
func4(func2)

from ch15t17c3 import c1var         #会运行在ch15t17c3中所有代码并得到c1var，如在此基础上再import其他变量则不必运行直接获得
print c1var         #通过ch15t17c3获得ch15t17c2，发现其中c1var的值和ch15t17c2代码书写的不同

# print X             #该部分不展示，因为如下述会多很多意义不明的输出。此方法可以用但一般按照书上340的方法用
# def func5():
#     import ch15t17c1                    #在函数内引用全局变量且不与本地同名变量发生冲突的方法1，注意因为运行了ch15t17会多很多输出
#     ch15t17c1.X += 1
#     print ch15t17c1.X
#     import sys                          #方法2。如果ch15t17模块已经import过则可以使用这种方法
#     thisMod = sys.modules['ch15t17c1']
#     thisMod.X += 1
#     print thisMod.X
#     X = 3
#     print X
#     return
# func5()             #如果注释掉func5的方法1则这里的调用会失败因为方法2中所需的模块未打开，但如果按书上的方法调用则会成功因为已经打开

def g():
    x = 1
    def h():
    # def h(x=x):       #成功，x通过默认参数被保存
    # def h(x=y):       #失败，def及参数列表和默认参数在def运行时被评估，此时y还没出现
        print x, y      #y能看到，因为代码块在函数运行时评估，此时y已经出现，def运行时不出现没关系
        # print z       #失败，因为代码运行时z还没出现
    y = 2
    h()
    z = 3
    extra()             #调用一个之后才定义的函数是可行的，只要运行g时extra已经定义好就行，因为那时g的定义才被验证
    return h
def extra():
    print 'extraFunc'
    return
h = g()
h()                     #x和y通过E作用域变量依赖被保存，可以在函数体中使用

L = []
for i in range(3):              #嵌套作用域中的变量在嵌套定义的函数被调用时才进行查找，所以循环定义多个函数不用默认参数会造成所有函数相同
                                #因为他们都看同一个变量名i
    L.append((lambda x:x*i))
print i                         #for不构成一个单独的命名空间，因此上面三个lambda函数所指向的i和这里的和下面的都是同一个，导致最后i=4，L[0](2)=2*4=8
for i in range(3,5):
    L.append((lambda x, i = i:x*i))     #解决方法是用默认参数因为它在def运行时评估，能记住当时值
print L[0](2), L[1](2), L[3](2), L[4](2)

def func6(x = []):              #可变默认值很危险，因为默认值是以单一对象实现的，多次调用函数看到的是同一个列表，这个列表的内容可能变化
    x.append(1)
    print x
    return
func6()                         #如此处所示，可变默认值导致调用函数时看到的默认的x不一致
func6()
def func7(x = None):            #这三行是上述问题的解决方法，注意本行x=None不可省略因为否则x会强制有值
    if x is None:
        x = []
    x.append(1)
    print x
    return
func7()
func7()

def func(a, b, c = 3, d = 3, *e, **f):          #顺序：无默认，有默认，*，**
    print a,b,c,d,e,f
    return
func(1, d = 4, e = 6, *[2], **{'g':4, 'h':5})
#顺序同上，先打散，再配顺序参数，再配关键字参数，*收集其他位置参数，**收集其他关键字参数，再配默认值，然后非*/**的参数要不重不漏则成功
#a顺序配1，b顺序配2，c默认配3，d关键字配4，e没收集到东西，f收集到e、g和h

print map((lambda (a,b):a), [(1,2),(3,4),(5,6)])    #lambda中只有一个元组参数，隐含序列赋值语句用于解析列表
import operator                                     #该模块提供内置表达式的函数
print map(operator.add, [1,5,9], [2,4,8])           #map将各个列表的元素取出来作为分开的参数调用函数

def gen(N):
    for i in range(N):
        yield i
    return
gen1 = gen(2)                   #一个生成器函数可以构造多个生成器对象
gen2 = gen(3)
gen3 = (i for i in range(3))    #生成器表达式类似列表解析，返回一个生成器
print gen1.next(), gen1.next(), gen2.next(), gen2.next(), gen3.next(), gen3.next()