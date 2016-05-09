# -*- coding: utf-8 -*-             #中文注释需要

import sys
print sys.path      #开头是模块文件位置，后面是PYTHONPATH，标准库，.pth可能有工作目录

import string       #按照sys.path搜索顺序，string系统库被本目录下自己写的string覆盖
import math         #奇怪的是sys和math却无法用上述方法覆盖，即使手动修改sys.path到只剩本目录都不行

ch18t21c3 = 33
import ch18t21c3 as c3, ch18t21c4 as c4         #展示as语法，对import或from有效，可以多个，逗号分隔。多个东西的import顺序执行
print ch18t21c3                                 #as过程基本等于import后赋值后del，但中间变量不会影响其他地方，如这里的ch18t21c3还是原来的值而没有被del
import ch18t21c2                                #import ch18t21c3时候ch18t21c2模块对象已经被导入在内存中，此处只是将其用变量名引用了出来
print ch18t21c2.inter, c3.ch18t21c2.inter, c4.inter, ch18t21c2.L, c3.ch18t21c2.L, c4.L
#12引用同一物，456引用同一物，解释见ch18t21c3、ch18t21c4

import ch18t21c2 as c2      #当内存中有模块对象时，这些代码只是用变量名引用了出来。由下句可见两个变量名都引用了同一个模块对象
print ch18t21c2 is c2

def func():
    import ch18t21c2 as c22     #这是第三个引用ch18t21c2的变量，不过也遵守变量作用域，所以下句注释解开则错
    print c22.inter
    return
# print c22.inter

print c2.__file__, c2.__name__  #__file__获得模块文件完整路径，__name__获得模块文件名称，但当作为顶层文件执行时候是“__main__”

inter = 1
print inter, c4.inter
c4.changeInter()        #操作ch18t21c4中的那个inter，不是本模块的，见ch18t21c4
print inter, c4.inter

c22 = reload(c2)        #reload的参数是引用已加载的模块对象的变量名，返回模块对象
print ch18t21c2 is c22, c22.inter, c3.ch18t21c2.inter, c4.inter, c22.L, c3.ch18t21c2.L, c4.L
#reload后内存中模块对象原地更新，以import.引用的都看得到。但原来from导入的看不到，因为reload重新赋值所以解除了共同引用，现在各引各的，别的新from旧

import dir1.dir2.pkg2   #包导入，每一段都会构造模块对象，目录的__init__会执行
# import dir1.dir3.pkg3 #解注释则错，无__init__.py的目录无法搜索
print dir1.dir2         #包导入的结果是把目录当成模块对象

from dir1.dir2 import * #dir1.dir2的__init__的__all__中的东西都会引入，包括pkg3模块
print dir2var, _dir2var
# print missDir2var     #解注释则错，这个没被导入

dir1.dir2.dir2var = 23
reload(dir1.dir2)       #目录构造的module也是module可以reload
print dir1.dir2._dir2var

import dir1.pkg2        #包引入允许同时使用多个同名模块

c2._X = 123             #获取属性的四种方法，注意sys.modules是个字典，要用模块名称而非引用模块的变量来索引
print c2._X, c2.__dict__['_X'], sys.modules['ch18t21c2']._X, getattr(c2, '_X')