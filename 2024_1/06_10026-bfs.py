# 10026 적록색약 BFS 접근
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
three_ans, two_ans = 0, 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  visited[x][y] = True

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
        visited[nx][ny] = True
        dq.append((nx, ny))

# 적녹색약이 아닌 경우
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i, j)
      three_ans += 1

# 적녹색약을 위해 배열 갱신(모든 R을 G로)
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'R':
      arr[i][j] = 'G'

visited = [[False]*N for _ in range(N)]

# 적녹색약인 경우
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i, j)
      two_ans += 1

print(f'{three_ans} {two_ans}')