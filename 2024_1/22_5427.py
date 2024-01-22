# 5427 불
import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
  sec = 0

  while sg_dq:
    sec += 1
    # 불이 이동할 장소 미리 처리
    while fire_dq and fire_dq[0][2] < sec:
      x, y, time = fire_dq.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
          if arr[nx][ny] == '.' or arr[nx][ny] == '@':
            arr[nx][ny] = '*'
            fire_dq.append((nx, ny, time + 1))

    # 상근이 이동 가능한 위치 찾기
    while sg_dq and sg_dq[0][2] < sec:
      x, y, time = sg_dq.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
          if arr[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            sg_dq.append((nx, ny, time + 1))
        else:
          return sec
  return 'IMPOSSIBLE'    

for _ in range(int(input().rstrip())):
  w, h = map(int, input().rstrip().split())
  arr = []
  for i in range(h):
    arr.append(list(input().rstrip()))

  sg_dq = deque() # 상근 위치 저장 Deque
  fire_dq = deque() # 불 위치 저장 Deque
  visited = [[False]*w for _ in range(h)]

  for i in range(h):
    for j in range(w):
      if arr[i][j] == '@':
        visited[i][j] = True
        sg_dq.append((i, j, 0))
      elif arr[i][j] == '*':
        fire_dq.append((i, j, 0))

  print(bfs())