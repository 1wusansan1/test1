'''
函数式编程 :
函数式编程是一种编程范式，强调使用纯函数（无副作用、不修改状态）和函数组合来构建程序。
Python作为一门多范式编程语言提供了一些函数式编程特性（由于Python允许使用变量，因此，Python不是纯函数式编程语言），如高阶函数、匿
名函数和函数组合，它们可以帮助我们编写简洁、可维护的代码。
使用python函数式编程的特点：
    函数可以赋值给变量，赋值后变量绑定函数。
    允许将函数作为参数传入另一个函数。
    允许函数返回一个函数。
'''
import random

print('================================================函数可以赋值给变量')


def fun():
    print('aaa')


fun()  # 调用函数
# l1 = [1,2,3]
var = fun  # 把函数fun绑定到var这个变量

var()  # 调用函数

print('================================================函数作为参数 ')


def fun1():
    print('aaa')


def fun2(func):
    func()
    print('bbb')


fun2(fun1)  # func = fun1  var=fun1

print('====================================作用：让你的程序灵活性更高。')


def fun1(item):
    if item > 30:
        return True
    else:
        return False


def fun2(item):
    if item % 2 == 0:
        return True
    else:
        return False


def fun3(item):
    i = 2
    while i < item:
        if item % i == 0:
            return False
        i += 1
    return True


def Filter(iterable, condition):
    for item in iterable:
        if condition(item):
            yield item


l1 = []
i = 0
while i < 100:
    l1.append(random.randint(10, 150))
    i += 1
print(l1)
for i in Filter(l1, fun1):
    print(i, end=' ')
print('================================================lambda表达式')
for i in Filter(l1, lambda item: item > 30):
    print(i, end=' ')
