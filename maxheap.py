"""
  Turn heapq's min-heap into a max-heap
"""
import heapq

def heapify(x):
    for i in range(0, len(x)):
        x[i] = -x[i]
    heapq.heapify(x)
def push(heap, item):
    heapq.heappush(heap, -item)
def pop(heap):
    return -heapq.heappop(heap)