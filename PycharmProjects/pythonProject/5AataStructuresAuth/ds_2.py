class StackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.__elems = []

    #判空
    def is_empty(self):
        return self.__elems == []
    #压栈操作
    def push(self,val):
        self.__elems.append(val)
    #弹栈操作
    def pop(self):
        if self.is_empty():
            raise  StackError('stack is already empty')
        return self.__elems.pop()
    #查看栈顶元素
    def top(self):
        if self.is_empty():
            raise  StackError('stack is already empty')
        return self.__elems[-1]


if __name__ == '__main__':
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)

    while s1.is_empty() == False:
        print(s1.pop(), end=' ')
    print()

    s1.top() #异常