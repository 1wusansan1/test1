'''
不可以修改
支持+ -乘除等运算
支持in not in
可索引，切片
'''

print(" ----------------------------------[定义]")
# 方式一 元组名 = (元素1, 元素2, 元素3)
t1 = (10, 20, 30)
# 方式二 元组名 = tuple( 可迭代对象 )
t2 = tuple("abcdefg")
t3 = tuple(range(10))
t4 = tuple(['A', 'B', 'C'])
# 小括号可以省略
t5 = 1, 2, 3
print(type(t5))
# ----------------------------------[索引]
print(" ----------------------------------[索引]")
# 变量 = 元组名[索引]
x = t1[0]
# 变量 = 元组名[切片] 元组[start:stop:step]
# 创建方式二
t2 = tuple("abcdefg")
print(t2[3])
print(t2[:5])
print(t2[2:])  # ('c', 'd', 'e', 'f', 'g')
print(t2[::-1])  # ('g', 'f', 'e', 'd', 'c', 'b', 'a')
print(t2[:-4:-1])  # ('g', 'f', 'e'
print(" ----------------------------------[遍历元组]")
t2 = tuple("abcdefg")
for c in t2:
    print(c, end=' ')
print()
for i in range(len(t2)):
    print(t2[i], end=' ')
    i = len(t2) - 1
print()
while i >= 0:
    print(t2[i], end=' ')
    i -= 1
print()
print(" ----------------------------------[api函数]")
t = (1, 2, 3, 3, 5, 8, 3, 3)
print(t.count(3))  # 统计指定元素在元组中出现的次数
print(t.index(3))  # 查找指定的元素在元组中第一次出现的位置 返回对应索引
print('t 中元素的个数: ', len(t))
print('t 中元素的最大值: ', max(t))
print('t 中元素的和值：', sum(t))
print(" ----------------------------------[拆包]")
# 拆包:　多个变量　= 容器
t = 1, 2, 3
a, b, c = t
print(f'{a} {b} {c}')
*a, b = t
print(f'{a} {b}')
print(" ----------------------------------[嵌套元组/列表]")
t = (1, 2, 3, ('a', 'b'), [4, 5, 6])
print(len(t))

print(" ----------------------------------[练习]")
year = input('请输入年份:')  # 2024  "2024" ---->2024
year = int(year)
month = int(input('请输入月份: '))
day = int(input('请输入日:'))
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
sum = 0
# 整月天数累加
for i in range(1, month):  # (1,2,.... month-1)
    sum += days[i - 1]
    # 不够1个月的天数
sum += day
if month > 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        sum += 1
print(f'{year}年{month}月{day}日是该年中第{sum}天')
