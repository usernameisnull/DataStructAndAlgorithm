#! /usr/bin/env python3
# encoding: utf-8
#   这特么是个 Binary Search tree  https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c
# 　还可以参考　https://github.com/TheAlgorithms/Python/blob/master/data_structures/Binary%20Tree/binary_search_tree.py
#   二叉查找树（BST：Binary Search Tree）是一种特殊的二叉树，它改善了二叉树节点查找的效率。二叉查找树有以下性质：
#   对于任意一个节点 n，
#      其左子树（left subtree）下的每个后代节点（descendant node）的值都小于节点 n 的值；
#      其右子树（right subtree）下的每个后代节点的值都大于节点 n 的值。
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                parent = current
                if node.data < parent.data:
                    if parent.left is None:
                        parent.left = node
                        return
                    else:
                        current = parent.left
                else:
                    if parent.right is None:
                        parent.right = node
                        return
                    else:
                        current = parent.right

    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def width_first(self):
        """
        宽度优先遍历
        :return:
        """
        to_visit = [self]
        while to_visit:
            current = to_visit.pop(0)
            if hasattr(current, "root"):
                current = current.root
            print current.data
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)


if __name__ == "__main__":
    '''
       Example
                     8
                    / \
                   3   10
                  / \    \
                 1   6    14
                    / \   /
                   4   7 13 
    '''
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)
    # 8 3 1 6 4 7 10 14 13
    # 先打印左边的===========================
    print t.root.data
    print t.root.left.data
    print t.root.left.left.data
    print t.root.left.right.data
    print t.root.left.right.left.data
    print t.root.left.right.right.data
    # 再打右边的==============================
    print t.root.right.data
    print t.root.right.right.data
    print t.root.right.right.left.data
    # 宽度优先遍历============================
    t.width_first()  # 8 3 10 1 6 14 4 7 13
