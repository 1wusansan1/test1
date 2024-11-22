
class QueueError(Exception):
    pass
class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        #head tail 都指向头节点
        self.__head = self.__tail = Node(None)
    def is_empty(self):
        return self.__head == self.__tail
    def enqueue(self,val):
        self.__tail.next = Node(val)
        self.__tail = self.__tail.next
    def dequeue(self):
        if self.is_empty():
            raise  QueueError('queue is already empty')

        val = self.__head.next.val
        self.__head = self.__head.next
        return val


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    while q.is_empty() == False:
        print(q.dequeue(), end = ' ')
    print()
