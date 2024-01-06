# 7562 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = (-2, -1, 1, 2, -2, -1, 1, 2), (-1, -2, -2, -1, 1, 2, 2, 1)

def bfs(x, y):
  dq = deque()
  dq.append((x, y))

  while dq:
    x, y = dq.popleft()

    if x == end_x and y == end_y:
      return arr[x][y]

    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < chess_len and 0 <= ny < chess_len and arr[nx][ny] == 0:
        arr[nx][ny] = arr[x][y] + 1
        dq.append((nx, ny))

for _ in range(int(input().rstrip())):
  chess_len = int(input().rstrip())
  arr = [[0 for _ in range(chess_len)] for _ in range(chess_len)]
  start_x, start_y = map(int, input().rstrip().split())
  end_x, end_y = map(int, input().rstrip().split())

  print(bfs(start_x, start_y))