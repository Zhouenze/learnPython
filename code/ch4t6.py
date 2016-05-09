# -*- coding: utf-8 -*-                                 #中文注释需要

M = [[1,2,3], [4,5,6], [7,8,9]]
print [row[1] + 1 for row in M if row[1] % 2 == 0]      #列表解析

print type(M) == type([]), type(M) == list, isinstance(M, list)         #类型检测，虽然这并不符合Python哲学

D = {'name':'zhouenze', 'gender':False, 'age':13}
for key in sorted(D):                                   #sorted用于满足迭代协议的对象，返回经整理的列表
    print key

print 5/-2.0, 5/-2, 5//-2.0, 5//-2                      #/浮点数正常整数下取整，//无论类型都下取整

print True + 1              #True和False就是显示不同的1和0

L1 = [1,[1,2]]
import copy
L2 = L1                     #完全互相影响
L3 = copy.copy(L1)          #除第一层外互相影响
L4 = copy.deepcopy(L1)      #全无影响
print L1 == L2, L1 is L2, L1 == L3, L1 is L3, L1 == L4, L1 is L4
L1[0] = 2
print L2, L3, L4
L1[1][0] = 2
print L2, L3, L4
L1 = 3
print L2, L3, L4

L1 = 3                      #缓存机制：小数字引用同一个，大数字全新建
L2 = 2 + 1
L3 = 31456423
L4 = 31456422 + 1           #优化机制：直接写31456423会指到同一个，用个表达式则不同
print L1 == L2, L1 is L2, L3 == L4, L3 is L4