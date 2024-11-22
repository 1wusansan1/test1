'''
Python 使用 lambda 来创建匿名函数 。 它可以具有任意数量的参数，但只能有一个表达式。
lambda 函数特点：
    lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
    lambda 函数主体是一个单个表达式，不能是语句块，这使得它们适用于编写简单的函数。
表达式即为匿名函数的返回值
表达式不能是赋值操作
lambda 语法格式：
    lambda arguments: expression
'''
f = lambda x, y: x + y
print(f(2, 3))  # 输出: 5

f = lambda: "Hello, world!"
print(f())  # 输出: Hello, world!

print('=============================高阶函数：将函数作为参数或返回值的函数。')

'''
内置高阶函数 :
    map（函数，可迭代对象）：使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；返回值为新可迭代对象。
    filter(函数，可迭代对象)：根据条件筛选可迭代对象中的元素，返回值为新可迭代对象。
    max(可迭代对象，key = 函数)：根据函数获取可迭代对象的最大值。
    min(可迭代对象，key = 函数)：根据函数获取可迭代对象的最小值。
    sorted(iterable, ***, key=None, reverse=False)， 排序
'''


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return str(f'eid:{self.eid},did:{self.did},name:{self.name},money:{self.money}')


# 员工列表
list_employees = [
    Employee(1001, 9002, "刘备", 60000),
    Employee(1002, 9001, "诸葛亮", 50000),
    Employee(1003, 9002, "曹操", 20000),
    Employee(1004, 9001, "贾诩", 30000),
    Employee(1005, 9001, "吕布", 15000),
]
print('=========================map 映射')
# 1. map 映射
# 需求:获取所有员工姓名
for item in map(lambda item: item.name, list_employees):
    print('map:', item)
print('=========================filter 过滤器')
# 2. filter 过滤器
# 需求：查找所有部门是9002的员工
for item in filter(lambda item: item.did == 9002, list_employees):
    print('filter:', item.__dict__)
print('=========================max min 最值')
# 3. max min 最值
emp = max(list_employees, key=lambda emp: emp.money)
print('max:', emp.__dict__)
print('=========================sorted')
# 4. sorted
# 升序排列
new_list = sorted(list_employees, key=lambda emp: emp.money)
for i in new_list:
    print(i)
# 降序排列
new_list = sorted(list_employees, key=lambda emp: emp.money, reverse=True)
for i in new_list:
    print(i)



