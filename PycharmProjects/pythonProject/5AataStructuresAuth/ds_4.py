
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__elems = []
    def is_empty(self):
        return self.__elems == []
    def enqueue(self,val):
        self.__elems.append(val)
    def dequeue(self):
        if self.is_empty():
            raise  QueueError('queue is already empty')
        return self.__elems.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    while q.is_empty() == False:
        print(q.dequeue(), end = ' ')
    print()
