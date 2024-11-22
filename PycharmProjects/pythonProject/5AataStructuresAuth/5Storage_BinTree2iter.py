'''
树型结构:
基本概念 :
    树（Tree）是n（n≥0）个节点的有限集合T，它满足两个条件：
        有且仅有一个特定的称为根（Root）的节点；
        其余的节点可以分为m（m≥0）个互不相交的有限集合T1、T2、……、Tm，其中每一个集合又是一棵树，并称为其根的子树（Subtree）。

    度数: 一个节点的子树的个数称为该节点的度数，一棵树的度数是指该树中节点的最大度数。
    树叶或终端节点: 度数为零的节点称为树叶或终端节点
    分支节点: 度数不为零的节点称为分支节点。
    一个节点的子树称为该节点的子节点，该节点称为它们的父节点，同一节点的各个子节点之间称为兄弟节点。
    一棵树的根节点没有父节点，叶节点没有子节点。
    节点的层数等于父节点的层数加一，根节点的层数定义为一。树中节点层数的最大值称为该树的高度或深度。
'''

'''
1.二叉树 
    二叉树（Binary Tree）是n（n≥0）个节点的有限集合，它或者是空集（n＝0），或者是由一个根节点以及两棵互不相交的、分别称为左子树和右子树的二叉树组
    成。二叉树与普通有序树不同，二叉树严格区分左孩子和右孩子，即使只有一个子节点也要区分左右。
    特征：
        二叉树第i（i≥1）层上的节点最多为2**(i-1)个。
        深度为k（k≥1）的二叉树最多有2**k -1个节点。
        满二叉树 ：每层节点数均达到最大值的二叉树。
'''

'''
二叉树的顺序存储实现 :
    二叉树本身是一种递归结构，可以使用Python list 进行存储。但是如果二叉树的结构比较稀疏的话浪费的空间是比较多的。
    空节点用None表示
    非空二叉树用包含三个元素的列表[d,l,r]表示，其中d表示根节点，l，r左子树和右子树。
'''

"""
思路分析:
 1. 使用链式结构存储二叉树的节点数据
2. 节点中存储 数据, 左孩子链接,右孩子链接 三个属性
"""


# 二叉树节点类
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树
class Bitree:
    def __init__(self, root):
        self.root = root

    # 前序遍历
    def preOrder(self, node):
        if node is None:
            return
        print(node.val, end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.preOrder(node.left)
        print(node.val, end=' ')
        self.preOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.preOrder(node.left)
        self.preOrder(node.right)
        print(node.val, end=' ')

'''
二叉树的遍历 :
    遍历是对树的一种最基本的运算，所谓遍历二叉树，就是按一定的规则和顺序走遍二叉树的所有节点，使每一个节点都被访问一次，而且只被访问一次。
    1. 前序遍历(DLR)
        首先访问根，再前序遍历左子树，最后前序遍历右子树。上图前序遍历的结果为： A B C D F G E H I 
    2. 中序遍历（LDR）
        首先中序遍历左子树，再访问根，最后中序遍历右子树。上图中序遍历的结果为：B A F D G C H E I 
    3. 后续遍历
        首先后序遍历左子树，再后序遍历右子树，最后访问根。上图后序遍历的结果为：B F G D H I E C A
'''
'''
              A
       B ------------- C
                  D ------- E
                F----G    H---I

# 前序遍历：（先根，再左子树，后右子树） ABCDFGEHI
# 中序遍历：（先左子树，再根，后右子树） BAFDGCHEI
# 后序遍历：（先左子树，再右子树，后根） BFGDHIECA
'''
if __name__ == '__main__':
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    h = Node('H')
    i = Node('I')
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 整个树根

    bt = Bitree(a)  # 把a作为根节点进行遍历
    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.postOrder(bt.root)

