# -*- coding: utf-8 -*-             #中文注释需要

class firstClass:                       #class是语句，产生类对象并赋值给变量名，执行Class时会执行其主体内每个语句
    name = 'firstClass'                 #class语句块内顶层无.赋值语句会构造类对象的属性，往往在此构造类对象的属性但并不强制
    L = [0,1,2,3]

    def setName(self, value):           #无法凭参数重载函数，def是执行语句，下面一个函数会覆盖这个函数因为对同一个变量名赋值
        pass
    def setName(fles):                  #self这个名称并不特殊，只是Python实例对象调用方法会将实例对象自动传入第一参数而这个参数惯例命名为self，所以至少1参数
        # print name                    #解注释则异常，因对无.变量的引用遵守LEGB，class构成命名空间而非作用域，不在LEGB中，无法搜索
        name = 'FirstClass'             #对无.变量的赋值就是本地作用域除非global，所以这里是新建变量不是操作class的name
        print name
        return
    def __init__(self, value):          #对类调用时运行以产生实例对象，常在此用self.attr表达式初始化实例对象
        print '__init__ of firstClass called'
        self.firstData = value

    def __add__(self, other):           #运算符重载，左侧为本类型时都调用这个，other为右
        print '__add__ called', other
        return
    def __radd__(self, other):          #左侧为其他类型右侧为本类型时调用这个，other为左
        print '__radd__ called', other
        return

    def __getitem__(self, item):        #能索引或能产生迭代器都可支持各种迭代工具，迭代器优先。索引是从0到异常依次索引，迭代器是next到异常
        return firstClass.L[item]
    # def __iter__(self):               #如果解注释迭代工具就会用迭代器运行，因为优先。缺陷是迭代器循环一次后失效要重做迭代器（往往隐含），索引则没这个问题
    #     print '__iter__ called'
    #     for i in range(4):
    #         yield firstClass.L[i]
    #     return

    def __call__(self, *args, **kwargs):    #拦截对实例的调用，可以此用实例对象模拟可保留状态的函数，此处状态就是self.firstData
        print self.firstData, args, kwargs
        return

    def addVar(self, value):
        self.var = value
    __var = 'firstClassVar'             #在继承他的类中会自动扩张成_firstClass__var以明确来源，减少冲突

firstObj = firstClass('firstObj')       #调用__init__，第一参数传入了实例对象，第二参数1
firstObj.setName()                      #没能修改firstClass.name
firstClass.name2 = 'firstClass2'        #任何对象（类对象、实例对象、函数对象……）本质都是命名空间，只要能引用都可自由地通过.表达式添加、修改、引用其属性
print firstClass.name, firstClass.name2

def setName2(firstAttr, secondAttr):    #方法就是函数对象，没什么特殊的，比如这里写个函数再用class.连接进去也一样用
    print firstAttr.firstData + ' in setName2 '
    firstClass.name = secondAttr        #不在类语句块顶层时，类对象中的属性只能用.表达式控制
    return
firstClass.setName2 = setName2
setName2(firstObj, 'Firstclass')        #简单函数形式调用，第一参数不传instance也行，成功修改
print firstClass.name
firstClass.setName2(firstObj, 'FirstClasS') #非绑定方法调用，第一参数要求传instance，成功修改，该方法可明确调用超类方法如superClass.__init__常用
print firstClass.name
boundedSetName2 = firstObj.setName2     #实例对象方法调用其实分两步，先像这样将实例对象绑定到方法构成绑定方法对象，常用于回调函数
boundedSetName2('FirstClass')           #然后由绑定方法对象调用，少一个参数因已绑定
print firstClass.name

del firstClass.name         #这句执行后下一句就挂，因为这个字符串对象只有唯一引用，本句导致他被回收
# print firstObj.name
del firstClass              #这句执行后下一句却没有什么问题，因为firstObj对firstClass有隐含引用，没了这个变量名的引用也不被回收
print firstObj.__class__.name2      #能看到firstClass对象的属性，实例对象的__class__引用其所属类对象
firstClass = firstObj.__class__     #实验做完，找回变量
firstClass.name = 'firstClass'

firstObj2 = firstClass('firstObj2')
firstObj + firstObj2, firstObj + 2, 2 + firstObj

for firstObj.iterObj in firstObj:   #for语句中隐含了多次对同一名称的赋值，这一名称可以是这种隐藏了实例对象属性的，for结束后仍有效，演示迭代
    print firstObj.iterObj
print firstObj.iterObj

firstObj.__dict__['iterObj'] = 'iterObj'    #对命名空间本身的（不含继承树）属性的引用和赋值等同于对其__dict__的索引和赋值
print firstObj.iterObj

firstObj(1,2,a=1,b=2)               #演示__call__

class secondClass(firstClass):
    def __init__(self):
        return
secondObj = secondClass()
secondObj.addVar('secondClassVar')          #调用了firstClass的addVar函数，其中的self.var赋值却赋给了本实例对象，因为查找到父类的方法并进行调用时其内部语句仍从调用实例出发进行解释
print dir(secondObj), secondObj.__dict__, secondObj._firstClass__var    #dir中自动包含继承到的变量名，观察变量名扩张

# #有关搜索顺序的两个实验
# # class A:
# class A(object):    #继承树中有object或内置类型则变成新式类，否则传统，但3.0后全部新式
#     x = 1
#     pass
# class B(A):         #连接别的命名空间并可搜索就是继承，命名空间的本质是字典，Python中的OOP其实就是在已连接的命名空间内寻找属性而已
#     x = 2           #属性搜索范围为继承树，由实例对象、所属类对象、所有连带父类对象构成，按继承树搜索顺序前面的覆盖后面的，所以若B有实例b则它先看到b的x再是B的2再是A的1
#     pass
# class C(A):
#     x = 3
#     pass
# class D(B, C):      #多根继承，称混合点
#     x = 4
#     # x = C.x         #想清楚些或者不想搞搜索顺序或者调整继承顺序也无法满足需求的话，在混合点明确指定就好，无论搜索还是引用都是如此
#     pass
# d = D()
# d.x = 0             #属性引用时搜继承树，属性赋值时在当前对象修改或新增，不会去操作树上被引用那个，所以下面是0,4
# print d.x, D.x
# #此处钻石继承结构，传统类以DBAC顺序搜索继承树，即深度优先，对多根继承由左至右；新类DBCA即在钻石继承结构中子类优先于共同超类
#
# class E():
#     x = 5
#     pass
# class F(E):
#     x = 6
#     pass
# class G(B, F):
#     x = 7
#     pass
# g = G()
# print g.x
# #对非钻石继承结构，传统类和新类搜索顺序一样都是深度优先从左至右

import pickle                                               #pickle的用法，注意binary
pickle.dump(setName2, open('pickleTest.txt', 'wb'))
setName2Copy = pickle.load(open('pickleTest.txt', 'rb'))
print setName2 == setName2Copy

import shelve                                               #shelve的用法，字典形式的数据库
db = shelve.open('shelveTest.txt')
db['setName2'] = setName2
db.close()
dbCopy = shelve.open('shelveTest.txt')
print dbCopy['setName2'] == setName2

class newClass(object):                     #演示新式类的新特性
    def getData(self):
        return self.__dict__['data']        #切忌self.data，死循环调用
    def setData(self, value):
        self.__dict__['data'] = value
        return
    data = property(getData, setData, None, None)
    #内容属性：对类对象来讲是一个引用property对象的名称，对类的实例来讲是一个搜索到类对象然后被拦截的变量名，
    #对它的赋值和引用等会交由指定函数处理（当然这些函数也可以明显地调用出来）

    @staticmethod               #函数装饰器，作用等同于下一句注释代码，将函数修改为静态函数，可以由类调用，就是一个用class.method方式调用的普通函数
    def staticMeth():
        print 'staticMeth called'
        return
    # staticMeth = staticmethod(staticMeth)
    @classmethod                #另一个内置函数装饰器，将函数改为类函数，由类调用，第一参数自动传入类对象
    def classMeth(cls):
        print 'classMeth called ', cls
        return

newObj = newClass()
# print newObj.data     #解注释则错，未定义__dict__['data']
newObj.data = 'data'    #赋值或直接调用setData均可
print newObj.data
newObj.setData('Data')
print newObj.data

newClass.staticMeth()   #静态函数和类函数调用
newClass.classMeth()

class rapper:                               #自制函数装饰器
    def __init__(self, func):               #调用那句等效语句（见下文）时产生本类实例并代替之
        self.func = func
        return
    def __call__(self, *args, **kwargs):    #本类实例对象替代了原有函数对象被调用
        print 'In rapper'
        self.func(*args, **kwargs)
        print 'Exit rapper'
        return
def rapper2(func):
    print 'In rapper2'
    return func
@rapper     #多层装饰器共用
@rapper2
def func(a,b,c):
    print a,b,c
func(1,2,3)