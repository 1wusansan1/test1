import random


class MyList(list):
    def __init__(self, it):
        super().__init__(it)
        self.arr = [x for x in it]


test1 = MyList("abcdefg")
print(len(test1))
print(dir(test1))
# print(test1.arr)
# print(test1.)
print('==================Integer=======add=================================')


class Integer:
    def __init__(self, value):
        self.data = value

    def __add__(self, other):

        if isinstance(other, Integer):
            return Integer(self.data + other.data)
        elif isinstance(other, int):
            return Integer(self.data + other)
        else:
            raise TypeError("类型不支持", type(other))

    # self.5AataStructuresAuth += other.5AataStructuresAuth
    # return self
    def __sub__(self, other):

        if isinstance(other, Integer):
            return Integer(self.data - other.data)
        elif isinstance(other, int):
            return Integer(self.data - other)
        else:
            raise TypeError("类型不支持", type(other))

    def __radd__(self, other):

        return self.__add__(other)

    def __rsub__(self, other):

        return Integer(other - self.data)

    def __str__(self):

        return str(self.data)


i1 = Integer(10)
i2 = Integer(20)
print(i1 + i2)
print(i1 - i2)
print(i1 - 5)
print(5 - i1)

print("===============================重写===============打印输出平均成绩 ???========avg!!!")


def average(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    sum = sum / len(l)
    return sum


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'我的名字是{self.name}, 我今年{self.age}, 考试考了{self.score}'

    def __repr__(self):  # 转成专业字符
        return 'Student("%s", %d,  %f)' % (self.name, self.age, self.score)

    def __add__(self, other):
        if isinstance(other, int):
            return Student(self.name, self.age, self.score + other)
        elif isinstance(other, float):
            return Student(self.name, self.age, self.score + other)
        elif isinstance(other, Student):
            return Student(self.name, self.age, self.score +
                           other.score)
        else:
            raise TypeError("类型不支持", type(other))

    def __radd__(self, other):

        return self.__add__(other)

    def __truediv__(self, other):
        return Student('平均成绩', self.age, self.score / other)


l3 = [Student('张飞', 26, 87.6), Student('赵云', 24, 98.2), Student('关羽', 28, 72.7)]
print(average(l3))  # 打印输出平均成绩 ???

print('-==========str=========get/setsetitem======contains==================================')


class MyList:
    def __init__(self, it):
        self.arr = [x for x in it]

    def __str__(self):
        return str(self.arr)

    def __getitem__(self, item):
        if item >= len(self.arr):
            raise IndexError('越界')
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __contains__(self, item):
        return item in self.arr


l1 = MyList("abcd")
print(l1) # __str__
l1[0] = 'A' # __setitem__
print(l1[0]) # __getitem__
if 'm' in l1: # __getitem__(用get获取一个一个的元素判断) / __contains__（用contains判断）
    print('在其中')
else:
    print('不在其中')

print('===========================================作业：在下面代码的基础上，让Student对象支持int(s1), 支持float(s1)操作， 分别返回age 和 score.')
'''
在下面代码的基础上，让Student对象支持int(s1), 支持float(s1)操作， 分别返回age 和 score.
'''


class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'我的名字是{self.name}, 我今年{self.age}, 考试考了{self.score}'

    def __repr__(self): # =====================================repr返回专业的字符串语句
        return 'Student("%s", %d, %f)' % (self.name, self.age, self.score)

    def __int__(self):
        return self.age

    def __float__(self):
        return self.score


s1 = Student("赵云", 22, 98.6)
print('dir(s1):', dir(s1))
str1 = str(s1)
print('s1:', s1)
print('str(s1):', str1)
print('repr(s1):', repr(s1))
# print(eval('1+2+3')) ==============================eval(str) 把str当作执行具体的python语句执行
s2 = eval(repr(s1))
print('eval(repr(s1)):', type(s2))

print('int(s1):', int(s1))
print('float(s1):', float(s1))
