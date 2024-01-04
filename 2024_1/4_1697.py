# 1697 
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  dq = deque()
  dq.append(N)

  while dq:
    x = dq.popleft()
    if x == K:
      print(weight[x])
      break
    for nx in (x-1, x+1, x*2):
      if 0 <= nx <= MAX and not weight[nx]:
        weight[nx] = weight[x] + 1
        dq.append(nx)

MAX = 10**5
N, K = map(int, input().rstrip().split())
weight = [0] * (MAX + 1)

bfs()