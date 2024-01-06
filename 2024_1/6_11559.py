# 11559 Puyo Puyo
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

arr = [list(input().rstrip()) for _ in range(12)]
ans = 0

# 상하좌우로 동일한 블록들을 탐색하는 BFS 함수
def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  visited[x][y] = True
  tmp = [(x, y)] # 동일한 블록의 좌표를 담을 리스트

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x+ dx[i], y + dy[i]
      if 0 <= nx < 12 and 0 <= ny < 6 and arr[x][y] == arr[nx][ny] and not visited[nx][ny]:
        dq.append((nx, ny))
        visited[nx][ny] = True
        tmp.append((nx, ny))
  return tmp

# 동일한 블록 제거 함수
def delete(tmp):
  for x, y in tmp:
    arr[x][y] = "."

# 블록을 아래로 내리는 함수
def down():
  for y in range(6): # 역순으로 순회
    for x in range(10, -1, -1):
      for k in range(11, x, -1):
        if arr[x][y] != "." and arr[k][y] == ".":
          arr[k][y] = arr[x][y]
          arr[x][y] = "."

while True:
  flag = False
  visited = [[False] * 6 for _ in range(12)]

  for x in range(12):
    for y in range(6):
      if arr[x][y] != "." and not visited[x][y]:
        tmp = bfs(x, y)
        # 동일한 블록이 4개이상일 경우 블록을 터트린다.
        if len(tmp) >= 4:
          flag = True
          delete(tmp)

  if flag:
    down()
    ans += 1
  else:
    break

print(ans)