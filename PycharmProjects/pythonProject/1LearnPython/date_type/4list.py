'''
可以修改
可索引切片
'''
import copy

l1 = ["a", "b", 'c']
l1.insert(2, "A")
# list 倒叙 -1代表最后一个元素，-2倒数二个元素以此类推
l1[-1] = "C"
print(l1[-1], end=' ')
print(l1[1], end='\n')
print(l1, end=' ')
print()
print('-' * 20)
# list 添加元素
l2 = list("sfmdk")
print("l2[1]:", l2[1])
l2.append("FF")
print("l2:", l2)

# 切片访问,左闭右开,list[start,stop,step]
print("切片访问1:4:", l2[1:4])
print("切片访问1:4:1:", l2[1:4:1])
print("切片访问1:4:2:", l2[1:4:2])
print("切片访问-4:-1:1:", l2[-4:-1:1])  # 正序只能从左往右，-4 -3 -2
print("切片访问-1:-4:-1:", l2[-1:-4:-1])  # step=-1代表倒叙1布从右向左-1，-2，-3
print("切片访问1:", l2[1:])
print("切片访问1::2", l2[1::2])
print("切片访问-1:", l2[-1:])
print("切片访问-1:", l2[-1::-1])
print('-' * 20)
for i in range(len(l2) - 1, -1, -1):  # 逆序
    print(l2[i])
print('-' * 20)
# 删除元素
l3 = list("sfmdkdff")
l3.remove('f')
print(l3)
del (l3[:3])
print(l3)
print('-' * 30)
# list运算 + - * / == != > <
print(l1 + l2)
print(l1 * 3)
print(l1 == l2)
# in not in
print('1' in l1)

# 列表的赋值，a = b指向同一个list,b修改元素值后，a的值也跟着改变，地址是一样的
a = list(range(10, 50, 10))
print(a)
b = a
b[0] = 11
print(a)
print("浅拷贝1", '-----------------------------------------' * 20)
# 列表的拷贝1 ，a拷贝给b指向不同list,a的值不会跟着改变，地址是不一样的
a = list(range(10, 50, 10))
print(a)
b = a[:]  # 拷贝
b[0] = 11
print(a)
print("浅拷贝2", '--------------------------------------------' * 20)
# 列表的浅拷贝2
l1 = ['北京', ['上海', '深圳']]
l2 = l1[:]  # 拷贝
l2[0] = '首都'
print(l1)
l2[1][0] = '魔都'  # 深层受影响
print(l1)
#
print("深拷贝", '--------------------------------------------------' * 20)
# 深拷贝
ll1 = ['北京', ['上海', '深圳']]
# print(len(l1))
ll2 = copy.deepcopy(ll1)  # 深拷贝
print(ll1)
ll2[1][0] = '魔都1'
print(ll1)

print("列表推导式 list = [x+10 for x in list0] / list = [x+10 for x in list0 if x > 10]",
      '--------------------------------------------------' * 20)
a = list(range(10, 50, 10))
print(a)
b = [x + 10 for x in a]
print(b)
b = [x + 10 for x in a if x % 3 == 0]  # 不满足if条件的元素会被删除
print(b)
print("列表嵌套推导式: list3 = [m + n for m in list1 for n in list2]", '--------------------------------------------------' * 20)
a = ['a', 'b', 'c']
b = ['A', 'B', 'C']
print("a:", a)
print("b:", b)
c = [m + n for m in a for n in b]
print("c:", c)



l1 = [1,2,3,[4,5,6]]
l2 = l1 # [1,2,3,[4,5,6]]
l3 = l1[:] # [1,2,3,[4,5,6]]
l4 = copy.deepcopy(l1)
l2[3][0] = 400
print(l1[3][0]) # l1 = l3 = l2 = [1,2,3,[400,5,6]] l4 = [1,2,3,[4,5,6]]
l3[3][0] = 4000
print(l1[3][0]) # l1 = l3 = l2 = [1,2,3,[4000,5,6]] l4 = [1,2,3,[4,5,6]]
l4[3][0] = 40000
print(l1[3][0]) # l1 = l3 = l2 = [1,2,3,[4000,5,6]] l4 = [1,2,3,[40000,5,6]]