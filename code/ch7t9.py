# -*- coding: utf-8 -*-             #中文注释需要

abstr = 'a\n\nb'                    #内部存储形式为'a\\n\\nb'，命令行写repr(abstr)自动回显会看出
print repr(abstr)                   #repr即上述内部存储形式，经过print解释后\\改为\
print str('a\n\nb')                 #str即abstr形式，经过print解释后\n改为回车

abstr = 'abcde'
print abstr[:]                      #正常规则：从左到右，含左不含右，步长第三值，省略分别为0、len(可直接写进去)、1
print abstr[::-1]                   #当负步长时的特殊规则：省略分别等同len-1、-1(无法直接写进去)
print abstr[0:5:-1], abstr[4:0:1]   #无效情况：从左由步长无法向右走

print '%-08.3f..' % 1.23456         #单个元素格式化，左对齐，补零，总宽8，小数点后3位，浮点数
print '%s %s' % ('s1', 's2')        #多个元素格式化
item1 = 12
item2 = 'male'
print '%(item1)d %(item2)s' % vars()#按字典格式化，vars为当前所有变量构成的字典

L = []
L.append(1)
L.extend([2])       #append与extend的区别
print L
L[0:1] = 'spam'     #分片赋值：先删除分片部分，再替换为右边部分，因此未必要等长，但右边必须可迭代
print L
del L[0]            #del可以直接用于删除
print L

D = {}
D['name'] = 'zhouenze'          #赋值即可增加
D[1] = 2                        #任何不可变类型都可以作为键
print D.get('name'), D.get(3)   #get获取比较安全
print 'name' in D, 'nam' in D   #in可判断键存在性
print dict(zip(['key1','key2','key3'], [1,2,3]))            #从两个列表构建字典的方法，zip的效果就是下一行这样
print dict([('1','1'), (2,2), ('3',3)])                     #从键值对列表构建字典

print (40), (40,)               #(40,)是元组而(40)是表达式

print int('10\n'), eval('[1,2,3]')  #字符串转换为数字忽略空白；eval把字符串当代码运行，通用但慢而危险

L = range(5)
print L[-100:100]               #分片越界按正确边界执行
L[0:0] = [0]                    #插入，其后顺延
print L
L[0:-5] = [-5]                  #-5<0无效，按照0执行，即插入
print L

X = 'x'
Y = 'y'
X,Y = Y,X   #本句不是三个式子而是元组赋值，导致交换
print X,Y