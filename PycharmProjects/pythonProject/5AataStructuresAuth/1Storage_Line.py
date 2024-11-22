'''
数据元素之间的常见逻辑结构有哪些，物理结构有哪些？
逻辑结构:
    线性结构
    树形结构
    图结构（网状结构）
物理结构：
    顺序结构
    链式结构
'''

'''
1.线性顺序结构
    列表（其他语言称数组）是一种基本数据类型 。是按照顺序存储结构实现的。若将线性表L=(a0,a1, ……,an-1)中的各元素依次存储于计算机一片连续的存储空
        间，这种机制表示为线性结构的顺序存储。
    所以python编程时可以借助列表这种python内置的数据类型来描述线性结构的顺序存储，而且列表本身就提供了丰富的接口满足这种数据结构的运算。
    特点：
        逻辑上相邻的元素 ai, ai+1，其存储位置也是相邻的；
        存储密度高，方便对数据的遍历查找。
        对表的插入和删除等运算的效率较差。
'''
print('--------------------------------------线性顺序结构')

L = [1, 2, 3, 4]
L.append(10)  # 尾部增加元素
print('尾部增加元素:', L)
L.insert(1, 20)  # 插入元素
print('插入元素:', L)
L.remove(3)  # 删除元素
print('删除元素:', L)
L[4] = 30  # 修改
print('修改:', L)  # 查找
print('查找:', L.index(2))  # 查找

'''
2.线性链式存储实现
    将线性表L=(a0,a1,……,an-1)中各元素分布在存储器的不同存储块，称为节点，每个节点（尾节点除外）中都持有一个指向下一个节点的引用，
        这样所得到的存储结构为链表结构。
    特点：
        逻辑上相邻的元素 ai, ai+1，其存储位置也不一定相邻；
        存储稀疏，不必开辟整块存储空间。
        对表的插入和删除等运算的效率较高。
        逻辑结构复杂，不利于遍历。
'''
print('--------------------------------------线性链式存储实现')


# 创建节点类
class Node:
    """
    思路 : *自定义类视为节点类,类中的属性为数据内容
          *写一个next属性,用来和下一个 节点建立关系
    """

    def __init__(self, val, next=None):
        """
        val: 有用数据
        next: 下一个节点引用
        """
        self.val = val
        self.next = next


# 链式线性表操作类
class LinkList:
    """
    思路 : 生成单链表,通过实例化的对象就代表一个链表
          可以调用具体的操作方法完成各种功能
    """

    def __init__(self):
        # 链表的初始化节点,没有有用数据,但是便于标记链表的开端
        self.head = Node(None)

    # 初始化链表,添加一组节点
    def init_list(self, list_):
        p = self.head  # p 作为移动变量
        for i in list_:
            # 遍历到一个值就创建一个节点
            p.next = Node(i)
            p = p.next
            # 遍历链表

    def show(self):
        p = self.head.next  # p代表第一个有值的节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        p = self.head
        # p移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val)  # 最后添加节点

    # 头部插入
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入
    def insert(self, index, val):
        # 设置个p 移动到待插入位置的前一个
        p = self.head
        for i in range(index):
            # 如果index超出了最大范围跳出循环
            if p.next is None:
                break
            p = p.next
        # 插入节点
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def remove(self, val):
        p = self.head
        # p 移动,待删除节点上一个
        while p.next is not None and p.next.val != val:
            p = p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    # 通过索引获取对应节点的值
    def search(self, index):
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        # 循环移动p
        for i in range(index):
            if p is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val


if __name__ == "__main__":
    # 创建一个链表
    link = LinkList()
    # 初始化一组数据
    l = [1, 2, 3, 4]
    link.init_list(l)
    print(link.search(0))
    print('链表遍历')
    # 链表遍历
    link.show()
    print('insert')
    link.insert(2, 88)
    link.show()
    link.clear()
    print(link.is_empty())



