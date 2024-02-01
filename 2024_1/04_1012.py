# 1012 유기농 배추
from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
  dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
  dq = deque()
  dq.append((x, y))
  arr[x][y] = 0 # 방문 처리

  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
        dq.append((nx, ny))
        arr[nx][ny] = 0 # 방문 처리

for _ in range(int(input().rstrip())):
  M, N, K = map(int, input().rstrip().split())
  arr = [[0]*N for _ in range(M)]
  ans = 0

  for _ in range(K):
    X, Y = map(int, input().rstrip().split())
    arr[X][Y] = 1
  
  for m in range(M):
    for n in range(N):
      if arr[m][n] == 1:
        bfs(m, n)
        ans += 1

  print(ans)