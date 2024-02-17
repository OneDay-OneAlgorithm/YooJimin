import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  heap.append(int(input()))

max_heap = []
for i in heap:
  if i == 0:
    if len(max_heap) > 0:
      max_item = heapq.heappop(max_heap)[1]
      print(max_item)
    else: print(0)
  else: heapq.heappush(max_heap, (-i, i))