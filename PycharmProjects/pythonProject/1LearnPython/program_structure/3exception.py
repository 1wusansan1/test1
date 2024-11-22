'''
当异常发生时，程序不会再向下执行，而转到函数的调用位置。如果异常没有被捕获到，会向上层(调用处)继续传递，直到程序终止运行。
返回到调用位置，观察该位置是否有异常处理代码，如果没有继续向调用位置跳转

常见异常类型：
-- 异常基类Exception。
-- 名称异常(NameError)：变量未定义
-- 类型异常(TypeError)：不同类型数据进行运算。
-- 索引异常(IndexError)：超出索引范围。
-- 属性异常(AttributeError)：对象没有对应名称的属性。
-- 键异常(KeyError)：没有对应名称的键。
'''

'''
===============================>语法：
try:
    可能触发异常的语句
except 错误类型1 [as 变量1]：
    处理语句1
except 错误类型2 [as 变量2]：
    处理语句2
except Exception [as 变量3]：
    不是以上错误类型的处理语句
else: # else子句最多只能有一个。
    未发生异常的语句
finally: #finally子句最多只能有一个，如果没有except子句，必须存在。
    无论是否发生异常的语句
'''

'''=======================> 异常的产生（raise）&& 自定义异常类:
'''


class StuInfoError(Exception):
    def __init__(self, desc, errno):
        super().__init__(desc,errno)
        self.desc = desc
        self.errno = errno


class Stu: # 自定义异常类
    def __init__(self, name, age, score):
        self.name = name
        self.age = age  # 1 私有属性正常命名
        self.score = score

    # 如果外界需要读取该私有属性
    @property  # 2 加读相关的装饰器
    def age(self):  # 3 读相关的函数名称要和私有属性保持一致
        return self.__age  # 6 注意私有属性名称是带__的

    @age.setter  # 4 加写相关的装饰器
    def age(self, newAge):  # 5 读相关的函数名称要和私有属性保持一致
        if newAge < 0 or newAge > 100:
            raise StuInfoError('年龄不合法', 10001) #=================异常的产生（raise）
        else:
            self.__age = newAge  # 6 注意私有属性名称是带__的


while True:
    try:
        age = int(input("请输入学生年龄:"))
        score = float(input('请输入学生的成绩:'))
        s1 = Stu('张飞', age, score)
    except StuInfoError as e:
        print('e.args:', e.args)
        print('e.desc:', e.desc)
        print('e.errno:', e.errno)
    except Exception as e:
        print(e.args)
