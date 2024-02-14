# 11501 주식

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
  N = int(input().rstrip())
  cost = list(map(int, input().rstrip().split()))
  cost.reverse()
  max_cost = cost[0]
  total = 0

  for i in range(1, N):
    if max_cost < cost[i]:
      max_cost = cost[i]
      continue
    total += max_cost - cost[i]
  print(total)
