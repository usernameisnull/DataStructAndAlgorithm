# encoding: utf-8
"""
    来源: https://github.com/TheAlgorithms/Python/blob/master/data_structures/Heap/heap.py
    关于堆的解释: https://blog.csdn.net/juanqinyang/article/details/51418629
    python自带的heap模块: https://blog.csdn.net/minxihou/article/details/51857518
    堆的排序: https://www.cnblogs.com/chengxiao/p/6129630.html
    =======================================================
    http://bubkoo.com/2014/01/14/sort-algorithm/heap-sort/
    几个计算公式：

        Parent(i) = floor((i-1)/2)，i 的父节点下标
        Left(i) = 2i + 1，i 的左子节点下标
        Right(i) = 2(i + 1)，i 的右子节点下标

"""


class Heap(object):
    def __init__(self):
        self.h = []
        self.currsize = 0

    def left_child(self, i):
        """
        获取左边节点
        :param i:
        :return:
        """
        if 2 * i + 1 < self.currsize:
            return 2 * i + 1
        return None

    def right_child(self, i):
        """
        获取右边节点
        :param i:
        :return:
        """
        if 2 * i + 2 < self.currsize:
            return 2 * i + 2
        return None

    def max_heapify(self, node):
        """
        构建最大堆
        :param node:
        :return:
        """
        print ("---------------------------------------")
        print("node(old) = %s, self.h = %s" % (node, self.h))
        if node < self.currsize:
            m = node
            lc = self.left_child(node)
            rc = self.right_child(node)
            if lc is not None:
                print ("self.h[%s] > self.h[%s]" % (lc, m), self.h[lc] > self.h[m])
            if lc is not None and self.h[lc] > self.h[m]:
                m = lc
            if rc is not None:
                print("self.h[%s] > self.h[%s], " % (rc, m), self.h[rc] > self.h[m])
            if rc is not None and self.h[rc] > self.h[m]:
                m = rc
            if m != node:
                temp = self.h[node]
                self.h[node] = self.h[m]
                self.h[m] = temp
                print("m(new) = %s, node(old) = %s, self.h = %s" % (m, node, self.h))
                print("===========================================")
                self.max_heapify(m)

    def build_heap(self, a):
        """
        构建堆
        :param a:
        :return:
        """
        self.currsize = len(a)
        self.h = list(a)
        for i in range(self.currsize / 2, -1, -1):
            self.max_heapify(i)

    def get_max(self):
        """
        获得最大值
        :return:
        """
        if self.currsize >= 1:
            me = self.h[0]
            temp = self.h[0]
            self.h[0] = self.h[self.currsize - 1]
            self.h[self.currsize - 1] = temp
            self.currsize -= 1
            self.max_heapify(0)
            return me
        return None

    def heap_sort(self):
        """
        堆排序
        :return:
        """
        size = self.currsize
        while self.currsize - 1 >= 0:
            temp = self.h[0]
            self.h[0] = self.h[self.currsize - 1]
            self.h[self.currsize - 1] = temp
            self.currsize -= 1
            self.max_heapify(0)
        self.currsize = size

    def insert(self, data):
        self.h.append(data)
        curr = self.currsize
        self.currsize += 1
        while self.h[curr] > self.h[curr / 2]:
            temp = self.h[curr / 2]
            self.h[curr / 2] = self.h[curr]
            self.h[curr] = temp
            curr = curr / 2

    def display(self):
        print(self.h)


def main():
    """
                5
               / \
              /   \
             4     6
            / \   /\
           /   \ /  \
          3    7 2   8
         /
        /
       1
    :return:
    """
    l = [5, 4, 6, 3, 7, 2, 8, 1]
    h = Heap()
    h.build_heap(l)
    print "after build,l= "
    h.display()
    """
        每个子树的顶端值都大于其叶子节点的值, 最大堆
                8
               / \
              /   \
             7     6
            /  \   /\
           /    \ /  \
          3     4 2   5
         /
        /
       1
    """
    h.heap_sort()
    print "after sort,l= "
    h.display()


if __name__ == '__main__':
    main()
