# encoding: utf-8
"""
    https://blog.csdn.net/minxihou/article/details/51857518
"""
import heapq


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)  # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]  # 往堆中插入一条新的值
    print "查看堆中最小值,但是不弹出", h[0]
    print "找到最大值: ", heapq.nlargest(1, h)
    return [heapq.heappop(h) for _ in range(len(h))]  # #从堆中弹出最小值


print heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
