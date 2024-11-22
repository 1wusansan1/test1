'''
不可以修改
可索引切片
'''
print('abc"123"')  # abc"123"
print("i'am ok")  # iam ok
print("""ssdsds
sdsdsdsds""")
print("Hello \b World!")
# ------------------r""取消转义：原始字符串
a = r"C:\newfile\test.py"
print(a)
# ------------------变量替换
print("我叫 %s 今年 %d 岁!" % ('小明', 10))  # 我叫 小明 今年 10 岁!
name = '小明'
age = 15
print(f'我叫 {name} 今年 {age + 1} 岁')
# ----------------------------------切片访问语法
# 切片访问语法： str[start:stop:step]
str1 = "abcdefghijklmn"
print(str1[0])
print(str1[len(str1) - 1])
print(str1[-1])
print(str1[2:-1])
print(str1[::2])
print(str1[::-1])
# str1[0] = 'A'  #语法错误 字符串属于不可以修改的序列容器，跟元组一样
# str API函数
s1 = "abcdaefga"
print(s1.count("a"))
print(s1.count('a', 0, 5))
print(s1.count("abc"))
print(s1.endswith("fga"))
print(s1.find("da"))
print(s1.upper())

list01 = ["a", "b", "c"]
result = "-".join(list01)
print(result)  # a-b-c

# 使用一个字符串存储多个信息
list_result = "刘备,关羽,张飞".split(",")
print(list_result)

'''
在终端中,循环录入字符串，如果录入了'quit'则结束录入，并以'_'拼接录入的所有内
容.
 '''
# content = []
# while True:
#     item = input("请输入字符串: ")
#     if item != 'quit':
#         content.append(item)
#     else:
#         break
# str1 = '_'.join(content)
# print(f'用户输入：{str1}')
print("=====str0.find(i)=====================================")
str = 'shdsks'
list1 = list(str)
str0 = ''
for i in list1:
    if (str0.find(i) == -1):
        str0 += i
print(f"去重后的字符：{str0}")

# while True:
#     content = int(input("请输入数字: "))
#     print(f'{content} 对应的字符为: ', chr(content))
#
# while True:
#     content = input("请输入字符串: ")
#     if content == 'quit':
#         break
#     for c in content:
#         print(f'{c} 对应的unicode编码值为: ', ord(c))
