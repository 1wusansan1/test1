'''
导入方式
Python中一个 .py文件可以作为一个模块，多个模块放到一起，组成一个包。
Python中所有加载到内存的模块都放在sys.modules，
'''
print('============================================================1')
'''模块导入方式一 import：
1. import fibonacci
fibonacci.fib1(12)
2. import fibonacci as fib
fib.fib1(100)
'''
import fibonacci

fibonacci.fib1(12)
print('============================================================2')
'''模块导入方式二 from class import method/*：
from fibonacci import fib1
fib1(100)   #调用时不用再使用模块前缀.method
缺点：：容易造成名字冲突。如果我导入了两个模块，这两个模块中存在同名的函数，那就是名字冲突
'''
from fibonacci import fib1

fib1(100)

'''
==================================找不到模块的解决方式：
临时添加模块完整路径
import sys
 sys.path.append('xxx模块所在路径')
 import xxx
将模块保存到指定位置
print(sys.path)
将xxx.py文件拷贝到lib\site-packages目录
设置环境变量 PYTHONPATH
'''

'''
在模块导入时，模块的所有顶层语句都会执行。
    如果一个模块已经导入，则再次导入时不会重新执行模块内的语句。
'''

'''
常用内置模块
与python解释器交互的模块 。
python3.8.2官方汉化版文档-pdf/library.pdf：P1679
'''

import sys

print(sys.path)
print(sys.version)
sys.exit(1)

# import os
#
# print(os.getcwd())  # 获取当前路径
# os.chdir("C:")  # 切换路径 change dir
# print(os.getcwd())
# os.makedirs(r'.\a\b\c\d')  # 递归创建文件夹
# print(os.path.exists('a'))  # 判断指定的文件（夹是否存在）
# os.removedirs(r'.\a\b\c\d')  # 递归删除文件夹
# print(os.path.join(os.getcwd(), "happy"))  # 拼接路径

'''
自定义包的创建与使用
my_project/
 main.py
 package01/
     __init__.py
     module01.py
     module02.py
     
1.如果只需要单独导入包内某个单独模块，__init__.py 为空即可
a. 
 """
 main.py
 """
 import package01.module01
 package01.module01.func01()
 package01.module01.func02()
 
 b. 
 """
 main.py
 """
 from package01 import module01
 module01.func01()
 module01.func02()
 
 c.
 """
 main.py
 """
 from package01.module01 import func01
 from package01.module01 import func02
 func01()
 func02()
 
注意：当__init__.py 为空时， 导入的对象为包内的某个指定模块。本质上要使得module01.py文件的顶层代码被执行。

2.若想通过from 包名 import  *时限制只导特定的包内模块， 可以通过__all__列表指定包内哪些模块生效。
 __init__.py
 from . import module01
 from . import module02
 __all__ = ["module01"]

 """
 main.py
 """
 from package01 import *
 module01.func01()
 module01.func02()
 module02.func03()#NameError: name 'module02' is not defined
 module02.func04()#NameError: name 'module02' is not defined
 
'''
