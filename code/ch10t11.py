# -*- coding: utf-8 -*-             #中文注释需要

try:
    inte = int('11')        #正确运行
    print 'right'
except:
    print 'error'
else:                       #正确运行因此进入本段
    print 'fine'

try:
    inte = int('a11')       #抛出异常
    print 'right'           #因异常而跳过本句
except:                     #抛出异常因此进入本段
    print 'error'
else:
    print 'fine'

a,b,c=[1,2,3]               #序列赋值语句
print a,b,c

L = M = []
L = L + [1]                 #产生了新列表因此互不影响
print L,M
L = M = []
L += [1]                    #虽然也是加号但是优化为append因此影响，行为与L = L + 不同
print L,M

L = L.append(1)             #这种原处修改无返回值，L被丢失
print L

import sys
sys.stdout = open('fakeStdout.txt', 'a')        #标准输出重定向
print 'print to fakeStdout'                     #默认输出到标准输出因此被劫持
sys.stdout = sys.__stdout__                     #恢复标准输出
print 'print to true stdout no \\n ',           #恢复正常，末尾加,不换行
print >> open('fakeStdout.txt', 'a'), 1         #暂时重定向
print 'stdout still work'