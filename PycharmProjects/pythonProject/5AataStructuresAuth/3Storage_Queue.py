'''
队列 :
    队列是限制在两端进行插入操作和删除操作的线性表，允许进行存入操作的一端称为“队尾”，允许进行删除操作的一端称为“队头”。（先进先出）
'''

'''
squeue.py  队列的顺序存储
    思路 :
        1. 基于列表完成数据存储
        2. 对列表功能进行封装
        3. 列表的头部作为队头,尾部作为队尾
    功能: 入队(enqueue),出队(dequeue),判断队列为空
'''

print('----------------------------------------------------------队列的顺序存储')


# 自定义异常
class QueueError(Exception):
    pass


class SQueue:

    # 设置空列表作为队列存储空间

    def __init__(self):
        self.__elems = []

    # 判断队列是否为空

    def is_empty(self):
        return self.__elems == []

    # 入队

    def enqueue(self, val):
        self.__elems.append(val)

    # 出队

    def dequeue(self):
        if not self.__elems:
            raise QueueError("Queue is empty")
        return self.__elems.pop(0)


if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())

'''
lqueue.py 队列的链式存储
    重点代码
    思路:
    1. 基于链表构建队列模型
    2. 链表的开端作为队头, 结尾作为队尾， 初始化状态下head tail都指向一个空的节点 方便判空
    3. 对头队尾分别添加标记,避免每次插入数据都遍历链表
    4. 队头和队尾重叠时认为队列为空
'''
print('----------------------------------------------------------队列的链式存储')


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        # 队列操作


class LQueue:
    def __init__(self):
        # 定义队头,队尾
        self.head = self.tail = Node(None)

    def is_empty(self):
        return self.head == self.tail

    # 入队 rear动
    def enqueue(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    # 出队  front动
    def dequeue(self):
        if self.head == self.tail:
            raise QueueError("Queue is empty")
        # front移动到的节点已经出队
        self.head = self.head.next
        return self.head.val


if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())
    print(lq.dequeue())
