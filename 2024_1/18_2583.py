# 2583 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().rstrip().split())
colored = [[False]*N for _ in range(M)] # 색칠된 여부 저장
result = [] # 결과 값 저장 배열(size)

for _ in range(K):
  x1, y1, x2, y2 = map(int, input().rstrip().split())
  for i in range(x1, x2):
    for j in range(M - y1 - 1, M - y2 - 1, -1): # y2 ~ y1까지 색칠
      colored[j][i] = True

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  colored[x][y] = True
  size = 1 # bfs 조건을 만족하는 영역의 크기 값

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and not colored[nx][ny]:
        dq.append((nx, ny))
        colored[nx][ny] = True
        size += 1 # 인접한 색칠되지 않은 영역의 크기 + 1

  result.append(size) # 결과 값 저장하는 배열에 추가

for i in range(M):
  for j in range(N):
    if not colored[i][j]: # 색칠되어있지 않은 영역 bfs
      bfs(i, j)

result.sort() # 크기 순 정렬
print(len(result))
print(*result)