# BFS - 미로 탈출
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
  dq = deque()
  dq.append((x, y))

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
        arr[nx][ny] = arr[x][y] + 1
        dq.append((nx, ny))

  return arr[N-1][M-1]

print(bfs(0, 0))