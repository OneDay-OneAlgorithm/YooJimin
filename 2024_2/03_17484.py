# 17484 진우의 달 여행(Small)

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
dx = (-1, 0, 1)

def dfs(col, row, d, low, ans):
  if col == N - 1:
    return min(low, ans)
  
  for i in dx:
    if i != d:
      if 0 <= col < N and 0 <= row + i < M :
        low = dfs(col + 1, row + i, i, low, ans + arr[col+1][row+i])

  return low

low = int(10e9)
for i in range(M):
  low = min(dfs(0, i, 2, low, arr[0][i]), low)

print(low)