# 7576 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # M : 가로, N : 세로
box = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dq = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      dq.append((i, j)) # 순회할 값을 우선적으로 큐에 넣기

def bfs():
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
        box[nx][ny] = box[x][y] + 1
        dq.append((nx, ny))

bfs()

for i in box:
  for j in i:
    if j == 0:
      print(-1) # 토마토가 다 익지 못하는 경우
      exit(0)
  ans = max(ans, max(i))

print(ans - 1)