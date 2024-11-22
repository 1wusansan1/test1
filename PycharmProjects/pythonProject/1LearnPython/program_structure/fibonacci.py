# usr/bin/env python
'''
实现斐波那契数列相关函数
'''
import sys


def fib1(n):
    a, b = 0, 1
    while b < n:
        print(b,end = ' ')
        a, b = b, b + a
    print()
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, b + a
    return result

if __name__ == "__main__":
    result = fib2(1000)
    print(result)