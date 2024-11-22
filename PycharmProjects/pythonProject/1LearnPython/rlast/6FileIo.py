'''
文件IO :
IO， input/output, 指的是数据在内部存储器和外部存储器或其他周边设备之间的输入和输出，即数据在计算机系统和外部世界之间的交换过程。
IO密集型程序， 在程序执行中有大量IO操作，而CPU运算较少。消耗CPU较少，耗时长。
计算密集型程序， 程序运行中计算较多，IO操作相对较少。CPU 消耗多，执行速度快，几乎没有阻塞。
文件，是保存在持久化存储设备（硬盘、U盘、SD卡）上的数据。从功能角度分为文本文件、二进制文件。在Python中把文件视为一种类型的对象。
'''

print('=================================字节串')
str0 = '中国'.encode(encoding="utf-8", errors="strict")
print('encode:', str0)
# encoding,  编码的格式   具体支持的编码格式 可以参考 library.pdf P160 常用： utf - 8和 gb2312

#  字节串转换为字符串方法： str.decode()  / bytes.decode(str)
str1 = bytes.decode(str0, encoding="utf-8", errors="strict")
print('decode:', str1)
print('decode:', str0.decode(encoding="utf-8", errors="strict"))

'''
文件基本操作 :
文件基本操作包括： 打开文件、 读/写文件、 关闭文件
'''

open("1.txt", mode='w', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
'''
file,  指定要打开的文件名称（包含路径）
mode, 文件打开方式，共有12种情况
buffering ,缓冲模式的设置
encoding, 文本文件的编码格式

===mode:========================================
r 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。read
rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。# =====后续不用指定encoding
w 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。write创建新文件。 binary
wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 binary
w+ 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。append
ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
===========================================

不带b的操作的是字符串，读出和写入也就是字符串的形式，
带b的操作的是字节串，读出和写入也就是字节串的形式。
文本文件打开方式既可以选择文本方式也可以选择二进制方式。
像图片、音视频只能以二进制方式打开，读写的也就是字节串。
如果不知道要操作的文件是文本形式的还是二进制形式的，那就选二进制方式打开。
=================================================读文件：
读文件的三个函数、四种方式
read(size)
 #读取size个字符（字节）, 如果省略size，默认取值为-1，代表读取文件所有内容
readline(size)
 #每次读取一行（只对文本文件有效）.如果省略size,默认为-1,就表示读一行。如果指定size,就是最多读取个数
readlines(size)
 #读取文件中的每一行作为列表中的一项。如果省略size,默认为-1，则直接读取到文件末尾。如果指定size表示读取到size字符所在行为止
for line in file: #文件对象本身是一个可迭代对象
=================================================== 写文件 ：
写文件的两个函数
write(string)#把文本数据或者二进制数据块写入到文件中去
writelines(str_list) #将字符串列表写入到文件中去
==================================================关闭文件 ：
f.close() # 关闭文件
==================================================with语法 ：
with被称作上下文管理器。
使用 with 关键字,当离开with代码块时，系统可以自动调用f.close()方法.
语法格式：
    with 表达式 as 变量:
        语句块   #其中会使用到上面变量

'''
print('================ with 关键字==')
# 使用 with 关键字,当离开with代码块时，系统可以自动调用f.close()方法.
with open('1.txt', 'w') as f:
    f.write('hello')
print('============缓冲机制==')

'''
缓冲刷新条件：
1.缓冲区满了
2.行缓冲换行时会自动刷新
3.程序运行结束或者close关闭文件
4.调用flush()函数
'''
with open('1.txt', 'w', buffering=1) as f:
    f.write('hello\n')
    f.write('world')
print('programme over========行缓冲')

with open('1.txt', 'w') as f:
    f.write('hello')
    f.flush()
    f.write('world')
    f.flush()
print('programme over========调用flush()函数')

'''
文件偏移量 
记录文件读写操作的位置。正常打开文件是偏移值为0 ，每读写一次都会根据读写的长度自动调整该偏移值。
如果是追加写入打开文件，偏移位置默认就是文件的长度
tell（）# 获取文件偏移量大小
seek（offset, whence）#重新设置偏移位置
    # whence 取值有三种情况
        # SEEK_SET  0  定位到从文件开头算起偏移offset个字节的位置
        # SEEK_CUR  1  定位到从当前位置开始计算偏移offset个字节的位置
        # SEEK_END  2  定位到从文件结束开始偏移offset个字节的位置
#如果是文本方式打开的文件，whence的取值只能是SEEK_SET
#如果是二进制方式打开文件，whence三种取值都可用
'''

import os

with open('1.txt', 'w+', encoding='utf-8') as f:
    f.write("hello")
    f.write('world')
    f.seek(5, os.SEEK_SET)  # 设置从头开始偏移5个
    f.write('python')
    f.seek(0, os.SEEK_SET)  # 设置从头开始偏移0个
    content = f.read()
    print(content)  # hellopython
    print("programme over========文件偏移量")

'''
文件管理函数 
#获取文件大小
os.path.getsize(file)
 #查看文件列表
os.listdir(dir)
 #查看文件是否存在
os.path.exists(file)
 #判断文件是否为普通文件
os.path.isfile(file)
 #删除文件
os.remove(file)
'''
print('==================文件管理函数:')
print(os.path.getsize('1.txt'))
print(os.listdir(r'D:\projects\PycharmProjects\pythonProject\LearnPython\rlast'))
print(os.path.exists('1.txt'))  # True
print(os.path.isfile('1.txt'))  # True
print(os.path.isfile('rlast'))  # False
# os.remove('1.txt')


