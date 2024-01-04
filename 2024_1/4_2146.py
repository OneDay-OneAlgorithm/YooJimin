# 2145 다리 만들기

import sys
from collections import deque
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

# 섬과 섬 구분 bfs
def island_bfs(x, y):
  global cnt # 섬 개수 카운터
  dq = deque()
  dq.append((x, y))
  visited[x][y] = True
  arr[x][y] = cnt

  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and not visited[nx][ny]:
        visited[nx][ny] = True
        arr[nx][ny] = cnt
        dq.append((nx, ny))

# 육지 간 가장 짧은 거리 구하는 bfs
def cross_bfs(z):
  global answer # 거리 최솟값 저장 메모리
  dist = [[-1]*N for _ in range(N)] # 육지 간 거리 저장 배열
  dq = deque()

  for i in range(N):
    for j in range(N):
      if arr[i][j] == z:
        dq.append((i, j))
        dist[i][j] = 0
  
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      # 범위 체크
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue

      # 다른 육지를 만날 경우
      if arr[nx][ny] > 0 and arr[nx][ny] != z:
        answer = min(answer, dist[x][y]) # 기존 answer와 비교해 최솟값으로 갱신
        return

      # 바다 만날 경우 
      if arr[nx][ny] == 0 and dist[nx][ny] == -1: # arr[nx][ny] == 0 : 바다 의미
        dist[nx][ny] = dist[x][y] + 1 # dist 갱신(dist[x][y] + 1)
        dq.append((nx, ny))

N = int(input().rstrip())

arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 1
answer = sys.maxsize

for i in range(N):
  for j in range(N):
    if not visited[i][j] and arr[i][j] == 1:
      island_bfs(i, j)
      cnt += 1

for i in range(1, cnt):
  cross_bfs(i)

print(answer)