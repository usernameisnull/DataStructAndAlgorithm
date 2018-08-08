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


if __name__ == "__main__":
    #
    #                   a
    #                  /  \
    #                 b    c
    #                /\    /\
    #               d  e  f  g
    #
    #
    #
    t = Tree('a')
    t.insert_left('b')
    t.insert_right('c')
    t.get_left().insert_left('d')
    t.get_left().insert_right('e')
    t.get_right().insert_left('f')
    t.get_right().insert_right('g')
    print "打印============================"
    print t.get_val()  # a
    print t.get_left().get_val()  # b
    print t.get_right().get_val()  # c
    print t.get_left().get_left().get_val()  # d
    print t.get_left().get_right().get_val()  # e
    print t.get_right().get_left().get_val()  # f
    print t.get_right().get_right().get_val()  # g
