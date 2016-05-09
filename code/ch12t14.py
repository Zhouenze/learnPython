# -*- coding: utf-8 -*-             #中文注释需要

branch = {'spam':1,                     #Python中以字典选择形式写的多路分支
             'spp':2,                   #括号内可跨行，统一对齐推荐但并不必须
                 'sp':3}
print branch.get('sp', 'bad choice')    #get第二参数为默认值，即多路分支的default
print branch.get('sppp', 'bad choice')

print 0 and 3, 1 and 3, 0 or 0.0, 1 or 3, not 0, not 1      #and和or会返回得到结果的那个操作对象，比较和not返回True或False

for [a,b] in [(1,2),(3,4),(5,6)]: print a,b                 #隐含了序列赋值语句（复习：序列赋值语句）

L = range(3)            #对列表取迭代器调用next获得每一项
iterL = iter(L)
print iterL.next(); print iterL.next()
D = {1:2,3:4}           #对字典取迭代器调用next获得每个key
iterD = iter(D)
print iterD.next(); print iterD.next()

for i in iter(range(3)): print i                        #等同于for i in range(5)因为for隐藏调用了iter

print range(3), range(3,5), range(3,9,2)                #range的三种调用

print L
for x in L: x += 1                  #错误的修改方法：操作于x而不涉及L
print L
M = L
for i in range(len(L)): L[i] += 1   #正确但慢的修改，LM都被影响
print L, M
L = [x + 1 for x in L]              #由列表解析产生新列表的修改方法，快，但运行方式和上面不同所以M不被影响
print L, M

print zip([1,2], [4,5,6]), map(None, [1,2], [4,5,6])    #zip折叠按最短，map(None)折叠按最长

for (i,c) in enumerate(['1', '2']): print i, c          #enumerate迭代器返回(下标,内容)元组，不同于一般默认调用的iter，此处隐含了序列赋值

print [x + y for x in 'abc' if x < 'c' for y in 'def' if y < 'f' ]      #复杂形式的列表解析，多个for和if，相当于循环嵌套，左侧在外

def myFunc():
    "doc for my Func"   #文档字符串写在一开头就行，会被系统收集为__doc__属性，无论是module，函数还是类都一样
    return
print myFunc.__doc__
help(myFunc)            #PyDoc将文档字符串和其他收集的信息合起来展示，目前运行不通因为string被覆盖了，这是ch18t21的测试。想跑通的话删掉string文件就好
