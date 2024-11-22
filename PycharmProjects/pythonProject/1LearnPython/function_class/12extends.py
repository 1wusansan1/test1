'''继承:
语法:
    class 父类:
        def 父类方法(self):
        方法体
    class 子类(父类)：
        def 子类方法(self):
        方法体
    儿子 = 子类()
    儿子.子类方法()
    儿子.父类方法()
===============> 说明: 子类直接拥有父类的方法。注意父类的私有方法(__method)子类也是不能访问的。
'''

print('================================================继承')


class Person:
    def say(self):
        print("说话")


class Teacher(Person):
    def teach(self):
        self.say()
        print("教学")


class Student(Person):
    def study(self):
        self.say()
        print("学习")


t1 = Teacher()
t1.say()
t1.teach()
print('======================')
s1 = Student()
s1.say()
s1.study()
print('======================')
print(Teacher.__base__)  # 记录了父类
print(Student.__base__)

print('=============================================继承===子类如果没有构造函数，将自动执行父类的')
'''
语法:
class 子类(父类):
    def __init__(self,父类参数,子类参数):
        super().__init__(参数) # 调用父类构造函数
        self.实例变量 = 参数
        
说明:
子类如果没有构造函数，将自动执行父类的，
但如果有构造函数将覆盖父类的。此时必须通过super()函数调用父类的构造函数，以确保父类实例变量被正常创建。
'''


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# 子类有构造函数,不会使用继承而来的父类构造函数[子覆盖了父方法,好像它不存在]
class Student(Person):

    # 子类构造函数：父类构造函数参数,子类构造函数参数
    def __init__(self, name, age, score):
        # 调用父类构造函数 super(Student, self).__init__(name, age)
        super().__init__(name, age)
        self.score = score


p1 = Person("刘备", 22)
print(p1.name)
s1 = Student("关羽", 23, 100)
print(s1.name)
print(s1.score)
print('================================================内置函数')
'''内置函数：
isinstance(对象, 类型) : 返回指定对象是否是某个类的对象(实例)。eg:s1是Student的实例，也是person的间接实例
issubclass(类型，类型)：返回指定类型是否属于某个类型 的直接或间接子类。eg:Student是Person的子类
'''
print(isinstance(s1, Student))
print(isinstance(s1, Person))
print(issubclass(Student, Person))

print('========================继承========================方法重写')
'''方法重写： 
如果继承来的方法不满足要求，那在子类中可以重写该方法.如果想调用父类的同名方法，可以使用super()函数。
'''


class A:
    def fun1(self):
        print('aaaaa')


class B(A):

    def fun1(self):  # 子类重写父类方法
        super().fun1()  # 子类重写弗雷方法时，可以引用父类方法作为自己方法的一部分功能
        print('bbbbb')


b = B()
b.fun1()
print('======多继承=======================一个子类继承两个或两个以上的基类，父类中的属性和方法同时被子类继承下来。')
print(
    '=========多继承===子类对象同时调用父类同名的方法super(A, self)============按__mro__顺序从A后执行第一个 !!!============')
'''多继承: 
1.定义：一个子类继承两个或两个以上的基类，父类中的属性和方法同时被子类继承下来。
2.多继承中，子类对象同时调用父类同名的方法时会出现冲突，而调用顺序由方法解析顺序MRO（method resolution order）决定
    ：print(D.__mro__) #__mro__属性中包含了该类的父类列表顺序,
      默认super().printo()按__mro__顺序执行第一个，super(A, self).printo()按__mro__顺序从A后执行第一个 !!!
'''


# 定义一个父类
class A:
    def printo(self):
        print('----A----')


# 定义一个父类
class B:
    def printo(self):
        print('----B----')


# 定义一个子类，继承自A、B
class C(A, B):
    def printo(self):
        super(A, self).printo()  # 默认super().printo()按__mro__顺序执行第一个，super(A, self).printo()按__mro__顺序从A后执行第一个
        print('----C----')


obj_C = C()
obj_C.printo()

print(C.__mro__)  # __mro__属性中包含了该类的父类列表
