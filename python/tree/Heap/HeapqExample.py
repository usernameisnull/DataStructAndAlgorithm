# encoding: utf-8
# """
#     https://blog.csdn.net/minxihou/article/details/51857518
# """
# import heapq
#
#
# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heapq.heappush(h, value)  # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]  # 往堆中插入一条新的值
#     print h
#     # print "查看堆中最小值,但是不弹出", h[0]
#     # print "找到最大值: ", heapq.nlargest(1, h)
#     # return [heapq.heappop(h) for _ in range(len(h))]  # #从堆中弹出最小值
#
#
# heapsort([3,2,1,0])
class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)

print(h.heap)

# for i in range(10):
#     n = h.pop()
#     print(n)
#     print(h.heap)
