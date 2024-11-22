'''
传递给函数的实参分为两种类型:
不可变类型
    数值型(整数，浮点数)
    布尔值bool
    字符串str
    元组tuple
可变类型
    列表 list
    字典 dict
    集合 set

！！！区别：不可变类型的数据传参时，函数内部不会改变原数据的值。可变类型的数据传参时，函数内部可以改变原数据。！！！
'''


# str,dict 传参
def func01(p1, p2):
    p1 = "刘玄德"
    p2["关羽"] += 50


a = "刘备"
b = {"关羽": 100}
func01(a, b)
print(a)  # 刘备
print(b)  # {'关羽': 150} 字典值被改变


# list,list 传参
def func01(p1, p2):
    p1 = [100, 200]
    p2[:] = [300, 400]


a = [10, 20]
b = [30, 40]
func01(a, b)
print(a)  # [10, 20]  p1改的是变量本身 而不是指向列表
print(b)  # [300, 400]  p2[:]就是在访问列表了

print('==================传参：实参=====my_sub(*[3, 2])位置参数：实参用*将序列拆解后与形参的位置依次对应也可以')


def my_sub(x, y):
    print('mysum:', x, '---', y)
    return x + y
    my_sub(3, 2)


# my_sub(3)  # 语法错误
my_sub(*(3, 2))  # 实参用*将序列拆解后与形参的位置依次对应也可以
my_sub(*[3, 2])
my_sub(*"AB")

print('===================传参：实参======================print_str(**d)：字典**关键字参数')


def print_str(a, b, c):
    print("a 是", a)
    print("b 是", b)
    print("c 是", c)


print_str(1, 2, 3)  # 按位置顺序
print_str(c=3, a=1, b=2)  # 使用关键字  就可以不按顺序了
d = {"b": 2, "c": 3, "a": 1}
print_str(**d)  # **将字典拆解变为关键字参数
print('=====================传参：实参====================缺省参数')


def print_str(a=1, b=2, c=3):
    print(" a是", a)
    print(" b是", b)
    print(" c是", c)


print_str(3, 2, 1)
print_str()
print_str(a=3, c=1, b=2)
print_str(a=3)
print('====================传参：星号元组 形参=====================func01(*args)不定长参数')


# 位置实参数量可以无限
def func01(*args):  # *,在形参变量中起到的作用是组包位置参数  形组实拆
    print(args)


func01()  # 空元组
func01(1, 2, 34)  # (1, 2, 34)

print('====================传参：双星号字典 形参=============func01(*args)不定长参数')


# 关键字实参数量无限
def func01(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2}


func01(a=1, b=2)


# func01(1,2,3) # 报错
def func01(list_target):
    print(list_target)  # ?


def func02(*args):
    print(args)  # ?


def func03(*args, **kwargs):
    print(args)  # ?


def func04(p1, p2, *args, p4, **kwargs):
    print(p1, end=' ')  # ?
    print(p2, end=' ')  # ?
    print(p4, end=' ')  # ?
    print(args, end=' ')
    print(kwargs)  # ?


print('===========================func01')
func01([1, 2, 3])
print('===========================func02')
func02(*[1, 2, 3])
print('===========================func03')
func03(1, 2, 3, a=4, b=5, c=6)
print('===========================func04')
func04(10, 20, 111, 222, p4=30, p5=40)
print('===========================func04-2')
func04(*(10, 20), 111, 222, p4=30, p5=40)

'''
斐波那契数列： [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]'''


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib_list = []
for i in range(20):
    fib_list.append(fib(i))
print(fib_list)


def sun(n):
    if n == 1:
        return 1
    return n * sun(n - 1)


y = 1


def func():
    y = 100


func()
print(y)  # 1
print('=================global:可以把一个函数内部的变量声明为全局域变量/函数内部使用全局域变量==========')
x = 1


def func():
    global x  # 没有全局的x变量
    x = 100


func()
print(x)  # 100

print('===========================nonlocal: 作用，在内层函数修改外层嵌套函数内的变量')
def func1():
    x = 100
    def func2():
        nonlocal x
        x = 200
    print(x)  # 100
    func2()
    print(x)  # 200
func1()
