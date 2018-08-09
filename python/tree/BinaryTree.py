# encoding: utf-8
# 参考： http://www.bkjia.com/Pythonjc/1133215.html
# 参考： https://blog.yangx.site/2016/07/22/Python-binary-tree-traverse/  Python实现二叉树的递归非递归遍历


class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, val):
        node = Tree(val)
        if self.left is None:
            self.left = node
        else:
            node.left = self.left
            self.left = node

    def insert_right(self, val):
        node = Tree(val)
        if self.right is None:
            self.right = node
        else:
            node.right = self.right
            self.right = node

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def preorder_traversal(self):
        """
        前序遍历算法
        :return:
        """
        print self.get_val()
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        """
        后序遍历算法
        :return:
        """
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print self.get_val()

    def inorder_traversal(self):
        """
        中序遍历算法
        :return:
        """
        if self.left:
            self.left.inorder_traversal()
        print self.get_val()
        if self.right:
            self.right.inorder_traversal()

    def breadth_first_traversal(self):
        """
            宽度优先遍历
            参考：https://codereview.stackexchange.com/questions/191984/perform-bfs-on-a-binary-tree
        """

        # root = self.root if root is None else root
        to_visit = [self]
        while to_visit:
            current = to_visit.pop(0)
            print(current.val)
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)


if __name__ == "__main__":
    #
    #                   a
    #                  /  \
    #                 b    c
    #                /\    /\
    #               d  e  f  g

    t = Tree('a')
    t.insert_left('b')
    t.insert_right('c')
    t.get_left().insert_left('d')
    t.get_left().insert_right('e')
    t.get_right().insert_left('f')
    t.get_right().insert_right('g')
    print "手动'宽度优先'搜索打印============"
    print t.get_val()  # a
    print t.get_left().get_val()  # b
    print t.get_right().get_val()  # c
    print t.get_left().get_left().get_val()  # d
    print t.get_left().get_right().get_val()  # e
    print t.get_right().get_left().get_val()  # f
    print t.get_right().get_right().get_val()  # g
    print "前序遍历========================"
    t.preorder_traversal()
    print "后序遍历========================"
    t.postorder_traversal()
    print "中序遍历========================"
    t.inorder_traversal()
    print "'宽度优先搜索'算法打印==========="
    t.breadth_first_traversal()


