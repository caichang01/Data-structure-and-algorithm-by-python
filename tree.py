# -*- coding: utf-8 -*-


class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            # 此结点的子树还没有齐
            treeNode = self.myQueue[0]
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                # 如果该节点存在右子树，则将其丢弃
                self.myQueue.pop(0)

    # 前序遍历
    def front(self, root):
        if root is None:
            return
        print(root.elem)
        self.front(root.lchild)
        self.front(root.rchild)

    # 中序遍历
    def middle(self, root):
        if root is None:
            return
        self.middle(root.lchild)
        print(root.elem)
        self.middle(root.rchild)

    # 后序遍历
    def back(self, root):
        if root is None:
            return
        self.back(root.rchild)
        self.back(root.lchild)
        print(root.elem)

    # 层序遍历
    def level(self, root):
        if root is None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild is not None:
                myQueue.append(node.lchild)
            if node.rchild is not None:
                myQueue.append(node.rchild)


"""主函数"""
if __name__ == '__main__':
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)

    print('前序遍历')
    tree.front(tree.root)

    print('中序遍历')
    tree.middle(tree.root)

    print('后序遍历')
    tree.back(tree.root)

    print('层序遍历')
    tree.level(tree.root)
