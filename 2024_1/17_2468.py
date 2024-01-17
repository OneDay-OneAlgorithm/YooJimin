# 2468 안전영역
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
max_rain = max(map(max, arr))

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(x, y):
  global cnt
  dq = deque()
  dq.append((x, y))
  sink[x][y] = True
  cnt += 1

  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not sink[nx][ny]:
        sink[nx][ny] = True
        dq.append((nx, ny))

cnt_list = []

for rain in range(max_rain):
  cnt = 0
  sink = [[False for _ in range(N)] for i in range(N)] # 물에 잠긴 여부

  for i in range(N):
    for j in range(N):
      if arr[i][j] <= rain:
        sink[i][j] = True # 물에 잠기는 영역 체크
  
  for i in range(N):
    for j in range(N):
      if sink[i][j] == False: # 물에 잠기지 않는 영역의 경우
        bfs(i, j) # 영역 모두 잠겼다고 가정, 안전 영역 1 추가
  cnt_list.append(cnt)

print(max(cnt_list))