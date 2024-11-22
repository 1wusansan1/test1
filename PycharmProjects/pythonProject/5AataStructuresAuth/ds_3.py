class StackError(Exception):
    pass

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
       self.__top = None

    #判空
    def is_empty(self):
        return self.__top == None

    #压栈操作
    def push(self,val):
        self.__top = Node(val, self.__top)
    #弹栈操作
    def pop(self):
        if self.is_empty():
            raise  StackError('stack is already empty')
        val = self.__top.val
        self.__top = self.__top.next
        return val
    #查看栈顶元素
    def top(self):
        if self.is_empty():
            raise  StackError('stack is already empty')
        return self.__top.val


if __name__ == '__main__':
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)

    while s1.is_empty() == False:
        print(s1.pop(), end=' ')
    print()

    print(s1.top()) #异常