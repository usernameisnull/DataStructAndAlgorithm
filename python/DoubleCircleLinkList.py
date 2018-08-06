# encoding: utf-8

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleCircleLinkLikst(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            node.next = self.head
            node.prev = self.head.prev

            # 这2个顺序不能换
            self.head.prev.next = node
            self.head.prev = node

            self.head = node
        self.size += 1

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.add(data)
        else:
            node.next = self.head
            node.prev = self.head.prev

            # 这2个顺序不能换
            self.head.prev.next = node
            self.head.prev = node

        self.size += 1

    def insert(self, pos, data):
        if pos < 0:
            self.add(data)
        elif pos > self.size - 1:
            self.append(data)
        else:
            index = 0
            cursor = self.head
            while index <= pos - 1:
                index += 1
                cursor = cursor.next
            # cursor = cursor.next
            node = Node(data)
            node.next = cursor
            node.prev = cursor.prev

            cursor.prev.next = node
            cursor.prev = node

    def __str__(self):
        if self.is_empty():
            return "no data"
        else:
            cursor = self.head
            result = []
            while cursor.next is not self.head:
                result.append(str(cursor.data))
                cursor = cursor.next

            result.append(str(cursor.data))
        return '<->'.join(result)


if __name__ == "__main__":
    d = DoubleCircleLinkLikst()
    d.add(1)
    d.add(2)
    d.add(3)
    print d

    d1 = DoubleCircleLinkLikst()
    d1.append(4)
    d1.append(5)
    d1.append(6)
    print d1
    d1.insert(2, 7)
    print d1
