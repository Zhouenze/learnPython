# -*- coding: utf-8 -*-             #中文注释需要

import ch2t3c1                      #第一次import有效会运行，后面再import不会被运行，即使已经修改过
print  ch2t3c1.inputText            #上面的import是将spam作为一个整体引入，其内部元素要通过.访问

from   ch2t3c1 import  inputText, inputText2
print  inputText, inputText2        #本次import是将spam的inputText属性作为一个整体引入，直接访问

reload(ch2t3c1)                     #强制重新运行，需要已经import过，对付中途修改

print dir(ch2t3c1)                  #获取可用变量名列表