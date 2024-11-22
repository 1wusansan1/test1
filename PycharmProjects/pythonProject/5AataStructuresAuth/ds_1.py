class Node:
    '''
    单向链表中的一个节点
    '''
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkList:
    '''
    单向链表类
    '''
    def __init__(self):
        self.head = Node(None)
    def init_list(self, list_):
        p = self.head
        for i in list_:
            p.next = Node(i)
            p = p.next
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val, end='  ')
            p = p.next
        print()
    def is_empty(self):
        if self.head.next is None:
            return True
        else :
            return False
    def clear(self):
        self.head.next = None
    def append(self, val):
        p = self.head

        while p.next is not None:
            p = p.next

        p.next = Node(val)
    def insert(self, index, val):
        #找到要插入位置的前一个节点
        p = self.head
        i = 0
        while i < index:
            if p.next is None:
                break
            p = p.next
            i += 1
        #插入新节点
        node = Node(val)
        node.next = p.next #新节点指向链表中的后继节点
        p.next = node #前驱节点指向新创建的节点
    def remove(self,val):
        # 寻址val值对应节点的前驱节点
        p = self.head

        while p.next is not None and p.next.val != val:
            p = p.next
        #当while循环结束：面临两种情况
        #1 没找到对应的节点
        if p.next is None:
            raise ValueError('x not in link')
        #2 找到了 p中存储的是一个节点的地址
        p.next = p.next.next

    def search(self,val):
        # 查找指定val值的节点的索引编号
        p = self.head
        i = 0

        while p.next is not None:
            p = p.next
            if p.val == val:
                return i
            i += 1

        #未找到对应节点
        return  -1




if __name__ == '__main__':
    link = LinkList()
    link.init_list([1,2,3,4,5])
    link.show()
    # link.clear()
    # if link.is_empty() :
    #     print('链表空')
    # else :
    #     print('链表非空')
    link.append(6)
    link.show()
    link.insert(0, 7)
    link.show()
    link.remove(4)
    link.show()

    index = link.search(6)
    if index != -1:
        print(f'找到了: index={index}')
    else:
        print('未找到')



