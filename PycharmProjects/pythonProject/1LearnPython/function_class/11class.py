'''
对象/实例对象:self，实例方法/对象方法:能访问self和cls
类变量；
类方法@classmethod:
    能访问只能cls类变量、类方法，不能访问实例变量，实例方法。但实例方法可以调用类属性和访问类方法
    无需实例化即可访问类方法
静态方法@staticmethod:
    不能访问self和cls（实例和类属性）
    不需要被类实例化，可直接调用
'''
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def study(self):
        print(f"{self.name}在学习")

    # 《 ------------------============================-对象方法 ：self》
    def introduce(self):
        print(f'大家好，我是{self.name}, 今年{self.age}岁')


zf = Student("张飞", 18, '男')
zf.introduce()  # 大家好，我是张飞, 今年18岁
print(dir(zf))
print(zf.__dict__)

# ----------------------------------------class2----------------------------------------------------------
class ICBC:
    # 类变量
    total_money = 10000000

    # 《---===============================类方法 》 ： 能访问类变量
    @classmethod
    def print_total_money(cls):
        # print(f"总行剩余钱数{ICBC.total_money}")
        print(f"总行剩余钱数{cls.total_money}")

    # 实例变量
    def __init__(self, name, money):
        self.name = name
        self.money = money
        ICBC.total_money -= money

    # 《-------=========================- 静态方法/静态方法 》 ： 不能访问类变量 也不能访问实例变量
    @staticmethod
    def breif():
        print('中国第一大银行')


bjfh = ICBC('beijing', 80000)
shfh = ICBC('shanghai', 50000)
ICBC.print_total_money()
print(ICBC.total_money)
print(f'{bjfh.name} 现有资金: {bjfh.money}')
ICBC.breif()
