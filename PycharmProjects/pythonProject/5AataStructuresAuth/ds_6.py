class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BiTree:
    def __init__(self, root):
        self.root = root
    def preOrder(self, root):
        if root is None:
            return
        #访问根节点
        print(root.val, end=' ')
        #前序遍历左子树
        self.preOrder(root.left)
        #前序遍历右子树
        self.preOrder(root.right)
    def inOrder(self, root):
        if root is None:
            return
        #中序遍历左子树
        self.inOrder(root.left)
        #访问根节点
        print(root.val, end=' ')
        #中序遍历右子树
        self.inOrder(root.right)
    def postOrder(self, root):
        if root is None:
            return
        #后序遍历左子树
        self.postOrder(root.left)
        #后续遍历右子树
        self.postOrder(root.right)
        #访问根节点
        print(root.val, end=' ')

if __name__ == '__main__':
    #构建叶子节点
    b = Node('B')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')
    #构建非叶子节点
    d = Node('D', f, g)
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)

    #构建二叉树
    bt = BiTree(a)

    #前序遍历二叉树
    print("前序遍历: ", end=' ')
    bt.preOrder(bt.root)
    print()

    # 中序遍历二叉树
    print("中序遍历: ", end=' ')
    bt.inOrder(bt.root)
    print()

    # 后序遍历二叉树
    print("后序遍历: ", end=' ')
    bt.postOrder(bt.root)
    print()


