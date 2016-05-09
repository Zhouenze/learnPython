# -*- coding: utf-8 -*-             #中文注释需要

inter = 44
from ch18t21c2 import *
print str(inter) + ' Oops, my inter is missing!'    #from*的隐患：覆盖原有的同名变量

# print _X          #解注释则错，_开头的变量一般不会被from*导入，除非由__all__明确指定

inter = 4           #from语句为import后赋值，得到的是共同引用变量名，此句对不可变对象重新赋值的结果是指向新对象，不影响内存中的模块对象或其他人对该模块的引用
L.append(1)         #不同于上句，此处修改了可变对象，影响了内存中的模块对象，其他导入ch18t21c2的模块都可见

def changeInter():
    global inter
    inter += 1      #此处操作的inter为本文件中的inter，即使函数在另一个有inter全局变量的模块中运行也一样。函数的效果在所属模块中已经确定，不在运行时变化
    return