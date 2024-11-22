'''
迭代器与生成器
实现了__iter__方法的类，是可迭代对象类
实现了__next___方法的类， 是迭代器类。
实现了__iter__、__next___方法的类，就是生成器类。
============
0.yeild o  一条一条生成
1.断点：执行顺序
    F8:  代码一步一步向下执行，但是遇到了函数以后，不进入函数体内部，直接返回函数的最终的执行结果
    F7: 代码一步一步向下执行，但是遇到了函数以后，进入到函数体内部，一步一步向下执行，直到函数体的代码全部执行完毕。
'''
from collections import Iterable


def my_generator(n):
    i = 0  # 先从硬盘读取一条数据 （生成数据）

    while i < n:
        yield i  # 返回生成的数据
        i += 1  # 生成数据


gen = my_generator(5)
for i in gen:
    print(i, end=' ')  # 输出: 0 1 2 3 4

'''
============ 一、迭代器：
迭代：是指在不断重复反馈过程，其目的通常是为了逼近所需目标或结果。
    每一次对过程的重复称为一次“迭代”，而每一次迭代的结果又会作为下一次迭代的初始值，为下一次迭代建立基础，最终通过不断地重复这个过程，迭代会收敛到最优
        解或者无限接近最优解。
可迭代对象：是指能用 iter(obj)函数 返回迭代器的对象。像字符串、列表、字典、元组、集合这些都是可迭代对象。他们都可以执行如下类似动作：
    for i in [1,2,3,4,5]:
        print(i)
好像我们可以不断迭代从列表这个容器中取出元素，但事实上容器并不提供这种能力，而是迭代器赋予了容器这种能力。

================如何让自定义类对象成为可迭代对象？
那就需要该自定义类中要实现 __iter__ （）方法，该方法可以返回一个迭代器对象
要返回一个迭代器对象就要定义一个迭代器类,迭代器类中要实现__next__()方法，
__next__()方法要实现能够依次返回自定义对象中一个元素， 在没有下一项数据时触发一个 StopIteration 异常的功能。
'''
# for循环的原理
# for i in [1,2,3,4,5]:
#

my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)  # 调用的是my_list.__iter__方法
print(type(iterator))
while True:
    try:
        item = next(iterator)  # 调用iterator.__next__方法
        print(item)
    except:
        break

print('======================迭代器类===可迭代对象类=======')


class MyIterator:  # 迭代器类

    def __init__(self, lst):
        self.lst = lst
        self.cur = 0

    def __next__(self):  # 迭代器的标志函数
        if self.cur >= len(self.lst):
            raise StopIteration
        i = self.cur
        self.cur += 1
        return self.lst[i]


class MyIterable:  # 可迭代对象类

    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __iter__(self):  # 可迭代对象的标志函数
        return MyIterator(self.data)  # 返回一个迭代器


L1 = MyIterable(range(10, 50))
for i in L1:
    print(i)
'''
==========================================如何判断一个对象是可迭代对象：
'''
print('===================================如何判断一个对象是可迭代对象：')

string = "sss"
# 方式一
print(isinstance(string, Iterable))  # 返回True，表明字符串也是可迭代对象
# 方式二
print(iter(string))  # 输出<str_iterator object at 0x7f7510708af0>

stu = {'name': '张飞', 'age': 32, 'score': 89.8}
it = iter(stu)
while True:
    try:
        item = it.__next__()
        print(item, stu[item])
    except:
        break
print('===================================================二、生成器generator')
'''
==========================================================二、生成器generator
可迭代对象实现中：（实现了__iter__方法的类，是可迭代对象类，实现了__next___方法的类， 是迭代器类。）
实现了__iter__、__next___方法的类，就是生成器类。
生成器：它是用来创建可迭代对象的一种方式，能够动态(循环一次计算一次返回一次)提供数据的可迭代对象。
优势：在循环过程中，按照某种算法推算数据，不必创建容器存储完整的结果，从而节省内存空间。数据量越大，优势越明显。
     以上作用也称之为延迟操作或惰性操作，通俗的讲就是在需要的时候才计算结果，而不是一次构建出所有结果。
========================《生成器是一种特殊的迭代器》是一个实现了__iter__ 方法的迭代器。
======================== Python中有两种方式来创建生成器：使用生成器表达式和使用yield关键字定义生成器函数。

'''


class MyGenerator:  # 生成器类

    def __init__(self, stop_value):
        self.stop_value = stop_value
        self.num = 0

    def __iter__(self):  # 返回一个迭代器对象

        return self

    def __next__(self):
        if self.num >= self.stop_value:
            raise StopIteration
        tmp = self.num
        self.num += 1
        return tmp


# gen = MyGenerator(10)
# it = iter(gen) #获取可迭代对象的迭代器
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# for i in [0,1,2,3,4,5,6,7,8,9] 将所有的数据一次性生成放入内存
for i in MyGenerator(10):  # 要一个，生成一个
    print(i, end=' ')
print()
print('========= Python中有两种方式来创建生成器：1.使用生成器表达式 2.使用yield关键字定义生成器函数。')

'''
class MyGenerator:  #生成器类
    def __init__(self, stop_value):
        self.stop_value = stop_value
        self.num = 0
    def __iter__(self): #返回一个迭代器对象
        return self
    def __next__(self):
        if self.num >= self.stop_value:
            raise StopIteration
        tmp = self.num
        self.num += 1
    return tmp
gen = MyGenerator(10) #创建一个生成器对象
'''

print('==========================================使用yield定义生成器函数========================')


# =========使用yield定义生成器函数
# 生成器函数  yield+函数的形式等价于前面设计的类
def my_generator(stop_value):
    i = 0
    while i < stop_value:
        yield i
        i += 1
    # gen = my_generator(10) # 返回一个生成器对象
    # print(type(gen))


for i in my_generator(10):
    print(i, end=' ')
print()

print('=====================生成器表达式========================')
'''
生成器表达式使用的语法与列表推导式相似，但是它使用小括号()而不是大括号{}。 也称作元组推导式
语法： 变量 = (表达式 for 变量 in 可迭代对象 if 条件)
'''
gen = (x * x for x in range(10))  # 生成器对象
print(gen)
print(type(gen))
# 将数据一股脑都加载到了内存
print(tuple([0, 1, 4, 9, 16, 25, 36, 49, 64, 81]))
# 用一个生 生成一个
print(tuple(gen))
for i in gen:
    print(i)

print('====================================内置生成器函数:enumerate(可迭代对象)')
'''
# 内置生成器函数 
枚举函数enumerate 
'''
# 遍历可迭代对象时，可以将索引与元素组合为一个元组
l1 = ['a', 'b', 'c', 'd', 'e']
for item in enumerate(l1):
    print(item)
for index, value in enumerate(l1):
    print(index, value)


# ===========================自行实现一个enumerate
def my_enumerate(iterable):
    index = 0
    for val in iterable:
        yield (index, val)
        index += 1


l3 = list(range(100, 150, 2))
print(l3)
for index, value in my_enumerate(l3):
    if index % 2 == 0:
        l3[index] = value + 1
print(l3)

print('=======================================内置生成器函数: zip')
'''zip
生成器 
'''
list_name = ["曹操", "孙权", "刘备"]
list_age = [22, 26, 25]
l3 = [1, 2, 3, 4]
# for 变量 in zip(可迭代对象1,可迭代对象2)
# 将多个可迭代对象中对应的元素组合成一个个元组，生成的元组个数由最小的可迭代对象决定。
for item in zip(list_name, list_age, l3):
    print(item)
    # ('曹操', 22)
    # ('孙权', 26)
    # ('刘备', 25)

print('============================自行编程实现zip函数')
# ================================自行编程实现 zip函数
def my_zip(*args):
    # 获取所有可迭代对象中元素个数的最小值
    min_items = len(args[0])
    i = 0
    while i < len(args):
        if min_items > len(args[i]):
            min_items = len(args[i])
        i += 1
    # min_items决定了zip函数可以生成多少个元组
    i = 0
    while i < min_items:
        res = []
        for item in args:
            res.append(item[i])
        yield tuple(res)
        i += 1
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = ['A', 'B', 'C']
l4 = ['A', 'B', 'C']
for item in my_zip(l1, l2, l3, l4):
    print(item)
