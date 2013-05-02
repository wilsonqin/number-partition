#!/usr/bin/python
import maxheap

# let's initialize a heap, with the numbers from file
def build_heap(num_arr):
  #f = open(file, "r")
  #num_arr = [int(line.strip()) for line in f]
  #f.close()
  maxheap.heapify(num_arr)
  return num_arr

def run(num_arr):
  #print "Here is the heap: ", build_heap(file)
  #heap = build_heap(file)
  heap = build_heap(list(num_arr))
  elem1 = maxheap.pop(heap)
  elem2 = maxheap.pop(heap)
  while (elem2 != 0):
    maxheap.push(heap, abs(elem1 - elem2))
    maxheap.push(heap, 0)
    #print heap
    elem1 = maxheap.pop(heap)
    elem2 = maxheap.pop(heap)
  #print "elem2: ", elem2
  assert(elem2 == 0)
  assert(elem1 != 0)

  return elem1