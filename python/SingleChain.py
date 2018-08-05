# encoding: utf-8
"""
    单链表
        解释: https://zh.wikipedia.org/wiki/%E5%8D%95%E5%90%91%E9%93%BE%E8%A1%A8
        借鉴: https://blog.csdn.net/Marksinoberg/article/details/69310033
"""
from copy import deepcopy

class Node(object):
    """
    存储节点
    """

    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class SingleChain(object):
    """
    单链表
    """

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, value):
        """
        在后面添加一个元素
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.head is None or self.size == 0:
            self.head = new_node
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = new_node
        self.size += 1

    def __str__(self):
        cursor = self.head
        result = []
        while cursor is not None:
            result.append(cursor.data)
            cursor = cursor.next
        return "->".join([str(item) for item in result])

    def __getitem__(self, index):
        if index < 0 or index > self.size - 1:
            return None
        if self.head is None or self.size == 0:
            return None
        cursor = self.head
        count = 0
        while cursor is not None:
            if count == index:
                return cursor
            cursor = cursor.next
            count += 1

    def __setitem__(self, index, value):
        if index < 0 or index > self.size:
            return
        new_node = Node(value)
        self.size += 1
        if self.head is None or self.size == 0:
            self.head = new_node
            return
        if index == self.size:
            self[self.size - 1].next = new_node
            return
        if index == 0:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
        else:
            cursor = self[index]
            pre = self[index - 1]
            pre.next = new_node
            new_node.next = cursor

    def __iter__(self):
        self.cursor = self.head
        return self

    def next(self):
        """
        实现迭代
        :return:
        """
        temp = self.cursor
        if self.cursor is None:
            raise StopIteration()
        else:
            self.cursor = self.cursor.next
            return temp

    def __reversed__(self):
        """
        逆序
        :return:
        """
        if self.size <= 1:
            return
        prev = None
        cursor = self.head
        while cursor is not None:
            current = cursor
            cursor = cursor.next
            current.next = prev
            prev = current
        self.head = prev

    def __add__(self, other):
        """
        两个单链表相加, 1->2->3 + 4->5 = 168
        :param other:
        :return:
        """
        _self = deepcopy(self)
        _other = deepcopy(other)
        reversed(_self)
        reversed(_other)
        result = []
        for item in [self, other]:
            cursor = item.head
            count = 0
            add_result = 0
            while cursor is not None:
                add_result += cursor.data * (10 ** count)
                count += 1
                cursor = cursor.next
            result.append(add_result)
        return sum(result)


if __name__ == "__main__":
    s = SingleChain()
    s.append(1)
    s.append(2)
    s.append(3)
    print s.size
    print s
    print "取元素", "=" * 15
    print s[0].data
    print s[1].data
    print s[2].data
    print "设置元素", "=" * 15
    s[0] = -1
    s[1] = 11
    s[4] = 4
    print "反向", "=" * 15
    print s
    reversed(s)
    print s
    print "迭代", "=" * 15
    for item in s:
        print item.data

    print "相加", "=" * 15
    s1 = SingleChain()
    s1.append(1)
    s1.append(2)
    s1.append(3)
    s2 = SingleChain()
    s2.append(4)
    s2.append(5)
    print s2 + s1
