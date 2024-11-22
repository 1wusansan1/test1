'''
14.2 函数作为返回值
14.2.1 闭包
    Python中的闭包可以通过以下格式进行定义
    def outer_function(x):
        def inner_function(y): #闭包函数
            return x + y
        return inner_function ============================== # 注意这里不是函数的调用，没带小括号，而是返回内嵌函数

在这个例子中，outer_function就是外层函数，inner_function就是内层函数，它返回的是内层函数的引用。
当我们传入一个参数x给外层函数时，它会返回一个内层函数inner_function。
因为inner_function保留了外层函数中的变量x的状态，所以在调用inner_function时，我们可以继续使用这个变量。
=======================闭包的三要素：
                        1.必须有内嵌函数
                        2.内嵌函数必须引用外部函数中的变量
                        3.外部函数返回值必须是内嵌函数。
===================语法格式：
                    def 外部函数名(参数)：
                        外部变量
                        def 内部函数名(参数):
                            使用外部变量
                        return 内部函数名
                    变量 = 外部函数名(参数)
                    变量(参数) #调用内部函数
======这个内部函数就是被称作闭包函数:
        "闭"函数指的是该函数是内嵌函数 ，  "包"函数指的是该函数包含对外层函数作用域名字的引用（不是对全局作用域） 。
======================闭包主要是用作函数装饰器
函数装饰器decorator
'''


def outer_func(x):
    def inner_func(y):
        return x + y

    return inner_func


func = outer_func(5)
print(type(func))
print(func(3))  # 8
print('=========================================不带函数装饰器decorato时==========理解1')
import time


def log_time(func):
    def wrapper():
        print(time.ctime(), end=':')
        func()

    return wrapper


def user_login():
    print('用户登录了系统')


def user_logout():
    print('用户登出了系统')


# user_login = 新功能 + 旧功能
user_login = log_time(user_login)  # 调用闭包函数
user_logout = log_time(user_logout)
user_login()
time.sleep(1)
user_logout()

'''
装饰器本身就是一个闭包，它可以保留被装饰函数的状态信息，并在被装饰函数执行前后添加额外的功能。
语法格式如下：
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before the function is called.")
            func(*args, **kwargs)
                print("After the function is called.")
        return wrapper
    @my_decorator   
    def say_hello(): 
        print("Hello, world!")
    #使用my_decorator装饰了say_hello函数，使其添加了功能
    say_hello()
'''

print('===================================================函数装饰器decorator')
print('============装饰器本身就是一个闭包，它可以保留被装饰函数的状态信息，并在被装饰函数执行前后添加额外的功能。')
print('===========================================================函数装饰器 - 传参 - 参数不统一问题')


def log_time(func):
    def wrapper(*args, **kwargs):  # ====================*args,**kwargs
        print(time.ctime(), end=':')
        func(*args, **kwargs)  # ====================这里也要把*args,**kwargs

    return wrapper


@log_time  # 带上 函数装饰器 标识，表明是log_time的闭包函数
def user_login(role, name):
    print(f'{role}:{name}登录了系统')


@log_time
def user_logout(name):
    print(f'用户{name}登出了系统')


# user_login = 新功能 + 旧功能
user_login('管理员', "张三")  # 只需调用装饰器函数，实际执行的是内嵌的闭包函数
time.sleep(1)
user_logout("张三")
