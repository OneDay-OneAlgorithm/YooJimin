# 2667 단지 번호 붙이기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
results = [] # 단지 수의 개수 저장
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  arr[x][y] = 0 # 체크가 완료된 블록은 다시 0으로
  length = 1 # 단지 길이 1

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
        dq.append((nx, ny))
        length += 1
        arr[nx][ny] = 0

  results.append(length) # 단지 길이 results 배열에 넣기

for i in range(N):
  for j in range(N):
    if arr[i][j]:
      bfs(i, j)

results.sort()
print(len(results))
print(*results, end='\n')