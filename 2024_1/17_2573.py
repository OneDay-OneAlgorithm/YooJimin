# 2573 빙산
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

  dq = deque()
  dq.append((x, y))
  visited[x][y] = True
  sea_list = []

  while dq:
    x, y = dq.popleft()
    sea = 0

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
          sea += 1
        elif arr[nx][ny] != 0 and not visited[nx][ny]:
          dq.append((nx, ny))
          visited[nx][ny] = True

    if sea > 0:
      sea_list.append((x, y, sea))

  for x, y, sea in sea_list:
    arr[x][y] = max(0, arr[x][y] - sea)

  return 1

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
year = 0

ice = []
for i in range(N):
  for j in range(M):
    if arr[i][j]:
      ice.append((i, j))

while ice:
  visited = [[False]*M for _ in range(N)]
  del_list = []
  group = 0

  for i, j in ice:
    if arr[i][j] and not visited[i][j]:
      group += bfs(i, j)
    if arr[i][j] == 0:
      del_list.append((i, j))

  if group > 1:
    print(year)
    break

  ice = sorted(list(set(ice) - set(del_list)))
  year += 1

if group < 2:
  print(0)