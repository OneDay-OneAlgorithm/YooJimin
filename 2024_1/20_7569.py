# 7569 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split())
arr = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

dq = deque()
dx, dy, dz = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)

def bfs():
  while dq:
    x, y, z = dq.popleft()
    for i in range(6):
      nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
      if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
        # 방문하지 않은 토마토 중 익지 않은 토마토
        if not visited[nx][ny][nz] and arr[nx][ny][nz] == 0:
          arr[nx][ny][nz] = arr[x][y][z] + 1 # 익었다고 처리
          visited[nx][ny][nz] = True
          dq.append((nx, ny, nz))

# 모두 익지 않은 경우
for h in range(H):
  for n in range(N):
    for m in range(M):
      if arr[h][n][m] == 1 and not visited[h][n][m]:
        dq.append((h, n, m))
        visited[h][n][m] = True

bfs()

# 토마토 모두 익었는지 확인
for tomato in arr: # 층
  for tom in tomato: # 줄
    for t in tom: # 개별
      if t == 0: # 익지 않은 토마토 존재
        print(-1)
        sys.exit(0)
    day = max(day, max(tom)) # 모두 1일 경우 0 출력
