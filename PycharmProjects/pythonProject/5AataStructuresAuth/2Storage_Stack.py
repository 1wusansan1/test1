'''
栈:
    栈是限制在一端进行插入操作和删除操作的线性表（俗称堆栈），允许进行操作的一端称为“栈顶”，另一固定端称为“栈底”，当栈中没有元素时称为“空栈”。
    先进后出
'''

'''
1.栈的顺序存储实现
    stack.py  栈模型的顺序存储
    重点代码
    思路 :
        1. 顺序存储可以使用列表实现,但是列表功能丰富,不符合栈模型要求
        2. 将列表功能封装,实现顺序栈的类,只提供栈的操作功能
    功能: 出栈, 入栈,判断栈空,查看栈顶元素
'''

print('------------------------------------------栈的顺序存储实现')
# 自定义异常
class StackError(Exception):
    pass


# 顺序栈
class Stack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶元素
        self.__elems = []

    # 入栈
    def push(self, val):
        self.__elems.append(val)  # 按顺序追加
        # 判断栈空

    def is_empty(self):

        return self.__elems == []

    # 出栈

    def pop(self):

        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems.pop() # 先弹出最后一个元素

    # 查看栈顶
    def top(self):

        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems[-1]


if __name__ == '__main__':
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
    # st.pop()  # 此时数据已经全部弹空，无数据，再操作弹出报错

print('------------------------------------------栈的链式存储实现')
'''
1.栈的链式存储实现
    lstack.py 栈的链式模型
    重点代码
    思路:
        1. 通过节点存储数据达到链式存储的目的
        2. 封装方法,实现栈的基本操作(入栈,出栈,栈空,查看栈顶)
        3. top为栈顶,在链表的头作为栈顶位置 (不需要遍历)
'''


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链式栈模型
class LStack:
    def __init__(self):
        # top作为栈顶的标记
        self.__top = None

    def is_empty(self):
        return self.__top is None

    # 入栈
    def push(self, val):
        self.__top = Node(val, self.__top) # 新的值作为top,next指向上一个top
        # node = Node(val)
        # node.next = self.__top
        # self.__top = node

    # 出栈
    def pop(self):
        if self.__top is None:
            raise StackError("pop from empty stack")
        data = self.__top.val
        self.__top = self.__top.next
        return data

    # 查看栈顶元素

    def top(self):
        if self.__top is None:
            raise StackError("pop from empty stack")
        return self.__top.val


if __name__ == '__main__':
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    print(ls.pop())
    print(ls.pop())
