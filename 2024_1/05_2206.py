# 2206 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
# 경로 관련 배열
  # index 0 : 벽을 부수지 않고 가는 경로
  # index 1 : 벽을 부수고 가는 경로
path = [[[0, 0] for _ in range(M)] for _ in range(N)]

def bfs(x, y):
  dq = deque()
  dq.append((x, y, 0)) # x 좌표, y 좌표, 벽을 부순 횟수
  path[y][x][0] = 1

  while dq:
    x, y, break_cnt = dq.popleft()

    if (x, y) == (M - 1, N - 1):
      return path[y][x][break_cnt]

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < M and 0 <= ny < N:
        # 벽인 경우
        if arr[ny][nx] == 1 and break_cnt == 0:
          path[ny][nx][1] = path[y][x][0] + 1 # 벽을 부순 횟수 누적
          dq.append((nx, ny, 1))
        
        # 이동 가능 && 해당 break_cnt에서 방문하지 않은 노드의 경우
        if arr[ny][nx] == 0 and path[ny][nx][break_cnt] == 0:
          path[ny][nx][break_cnt] = path[y][x][break_cnt] + 1
          dq.append((nx, ny, break_cnt))

  return -1 # 불가능한 경우

print(bfs(0, 0))