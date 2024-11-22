'''
函数， 用于封装一个特定的功能，表示一个功能或者行为。
函数是可以重复执行的语句块, 可以重复调用。
'''


# return 跳出所有嵌套循环
# break 跳出第一层嵌套循环
# continue 跳出此次循环
def sum(n):
    """
   功能：计算1到n的累加和
   参数n：累加的最大值
   """
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def func03():
    print("func03执行了")
    return
    print("func03又执行了")  # 未执行


# 4. return 可以退出多层循环嵌套
def func04():
    while True:
        while True:
            while True:
                # break 只能退出一层循环
                print("循环体")
                return
        print("33333333")


def func04():
    print("call func04")
    return 1, 2, 3, 4  # 4 可以返回多个值 本质是返回了一个元组

b = func04()
print(type(b))
print(b)
m, n, x, y = func04()  # 自动拆包
print(m,n, x, y)
