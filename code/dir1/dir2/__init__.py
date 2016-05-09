# -*- coding: utf-8 -*-             #中文注释需要

print 'Init for dir2 called'

dir2var = 20
missDir2var = 22        #由于没有被包含在__all__中，这个变量无法用from*引入
_dir2var = 22
__all__ = ['dir2var',
           '_dir2var',  #如果没有__all__则_开头的变量不会被from*导入，但__all__权力更高
           'pkg3']      #当有__all__且其中包含本目录下的模块名时，模块会被from*连带导入