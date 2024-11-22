'''
可变(dict字典/list列表)
可修改
key是唯一的
不支持+ -乘除等运算
支持in not in
不能索引切片
clear()#清除字典中的元素
copy() #拷贝字典  注意是-->浅拷贝
get(key) #返回key对应的value
items() #返回所有的键值对
keys() #返回所有的key
vlaues() #返回所有的value
update()#更新字典
deepcopy()深拷贝
del dict('key')删除
'''
import copy

# 方式一：{ 键1:值1, 键2:值2 }
dict_lb = {"name": "刘备", "age": 32, "sex": "男"}
dict_gy = {"name": "关羽", "age": 30, "sex": "男"}
dict_zf = {"name": "张飞", "age": 28, "sex": "男"}
dict_empty = {}
# 方式二：dict(  [(  ,  ),( , )]  ) ， 列表元素必须能够"一分为二"
d1 = dict([("age", 20), ("name", 1)])
print(dict_lb)
print('====================================================修改、添加元素')
# ================================================================修改、添加元素
dict_lb["age"] = 35  # 已有的key 就是修改
dict_lb["salary"] = 10000  # 未有的key 就是添加
print('修改、添加元素:', dict_lb)
print('====================================================获取元素')
# ================================================================获取元素
# 字典不能索引、切片
print('如果没有获取的键则报错:', dict_lb["name"])  # 注意：如果没有键则报错
if "name" in dict_lb:
    print('name:', dict_lb["name"])
print(dict_lb)
print('====================================================遍历字典')
# ====================================================遍历字典
dict_lb = {"name": "刘备", "age": 32, "sex": "男"}
for key in dict_lb:
    print('for:', key)
for key in dict_lb.keys():
    print('for dict_lb.keys()遍历:', key)
for value in dict_lb.values():
    print('for dict_lb.values()遍历:', value)
for key, value in dict_lb.items():
    print('for dict_lb.items()遍历:', key, value)
print('====================================================删除元素')
# 删除元素
del dict_lb['sex']
print(dict_lb)
del dict_lb  # 删除整个字典变量
# print(dict_lb) del删除了变量报错

print('====================================================拷贝')
d1 = {1: 'a', 2: 'b', 3: 'c'}
print(d1)
d1.clear()  # 清空变量不报错
print(d1)
d2 = {1: ['a', 'b', 'c'], 2: ['A', 'B', 'C']}
print('d2:', d2)
d3 = d2.copy()  # 浅拷贝
d3[1][0] = 'm'
print('浅拷贝影响了d2:', d2)
d4 = copy.deepcopy(d2)
d4[1][0] = 'n'
print('深拷贝未影响d2:', d2)
print(d4.get(2))
d4.update({3: {'name': "zhangsan"}})
print('update d4:', d4)
