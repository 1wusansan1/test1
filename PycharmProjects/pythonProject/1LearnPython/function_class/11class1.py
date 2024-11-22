'''私有属性:
1.一个下划线的属性名（例如 _x）表示这个属性是受保护的，应该被视为私有属性，尽管它仍然可以被类的实例直接访问。
2.两个下划线的属性名（例如 __x）表示这个属性是真正的私有属性。这意味着在类的外部无法直接访问该属性，甚至子类也不能访问它。
3.__x__, 双下划线开头双下划线结尾的属性， 特殊属性，特殊用途。
'''
print('=============================================私有属性')


class Stu:
    def __init__(self, name, age, socre):
        self.name = name
        self.__age = age  # __age 变成了私有属性  ====类的外部是看不到 私有化的本质就是改名: _类名+属性名
        self.score = socre


s1 = Stu('张飞', 21, 80)
print(dir(s1))

# print(s1.__age)  # 语法会报错
# print(s1._Stu__age)  # 改了名字，一啊不能不这样用
print('=====================================s1.getAge()========外部访问私有属性的方式一')


class Stu:
    def __init__(self, name, age, socre):
        self.name = name
        self.setAge(age)  ## 或者 self.__age = age
        self.score = socre

    def getAge(self):

        return self.__age

    def setAge(self, newAge):

        if newAge < 0 or newAge > 100:
            raise ValueError('年龄不合法')
        else:
            self.__age = newAge


s1 = Stu('张飞', 21, 80)
# print(s1.__age) #语法会报错
# print(s1._Stu__age)
print(dir(s1))
s1.setAge(30)
print(s1.getAge())

print('============================外部访问私有属性的方式二： 通过装饰@property 和 <attribute_name>.setter来实现')


class Stu:
    def __init__(self, name, age, socre):

        self.name = name
        self.age = age  # ============== 1 私有属性正常命名
        self.score = socre

    @property  # ==============2 加读相关的装饰器
    def age(self):  # ==============3 get方法名同属性名一致

        return self.__age  # ==============4 注意(在读写函数中)私有属性名称是带__的，其他方法正常用age

    @age.setter  # ==============6 加写相关的装饰器
    def age(self, newAge):  # ==============5 get方法名同属性名一致

        if newAge < 0 or newAge > 100:
            raise ValueError('年龄不合法')
        else:
            self.__age = newAge

    # =====================================私有化方法,只能内部访问
    def __pres(self, value):
        return value + 5

    def __str__(self):
        return f'我的名字是：{self.name}, 我今年{self.age}岁，考了{self.score}'


s1 = Stu('张飞 ', 21, 80)
# print(s1.__age) #语法会报错
# print(s1._Stu__age)
print(dir(s1))
print(s1.age)
s1.age = 40
print(s1.age)
str1 = str(s1)
print(str1)
