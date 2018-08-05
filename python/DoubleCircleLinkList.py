# encoding: utf-8
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleCircleLinkList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append_left(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
            self.head.prev = new_node
            self.head=new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
            self.head.prev = new_node
            # self.head=new_node

    def __str__(self):
        if self.is_empty():
            return "no data"

        cursor = self.head
        result = []
        while cursor.next is not self.head:
            result.append(str(cursor.data))
            cursor = cursor.next
        result.append(str(cursor.data))
        return "<->".join(result)


if __name__ == "__main__":
    d = DoubleCircleLinkList()
    d.append_left(1)
    d.append_left(2)
    d.append_left(3)
    print d

    d2 = DoubleCircleLinkList()
    d2.append(1)
    d2.append(2)
    d2.append(3)
    print d2

