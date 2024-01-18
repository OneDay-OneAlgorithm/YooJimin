# 6593 상범빌딩
import sys
from collections import deque

input = sys.stdin.readline

dx, dy, dz = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)

while True:
  L, R, C = map(int, input().rstrip().split())
  if L == 0 and R == 0 and C == 0:
    break
  
  arr = []
  visited = [[[False]*C for _ in range(R)] for _ in range(L)]
  for _ in range(L):
    arr.append([list(input().rstrip()) for _ in range(R)])
    tmp = input().rstrip()

  dq = deque()
  escaped = False # 탈출 여부

  for i in range(L): # z축
    for j in range(R): # x축
      for k in range(C): # y축
        if arr[i][j][k] == 'S': # 시작 지점일 경우
          start = (i, j, k, 0) # 시작 좌표, 누적 시간 저장
          visited[i][j][k] = True
        if arr[i][j][k] == 'E': # 종료 지점일 경우
          end = (i, j, k) # 종료 좌표 저장
  
  dq.append(start) # 시작 지점 추가

  while dq:
    z, x, y, min = dq.popleft()
    if (z, x, y) == end: # 종료 지점과 현재 좌표가 같을 경우
      escaped = True # 탈출 성공
      print(f'Escaped in {min} minute(s).')
      break

    nmin = min + 1

    for i in range(6):
      nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
      if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and not visited[nz][nx][ny]:
        if arr[nz][nx][ny] == '.' or arr[nz][nx][ny] == 'E':
          dq.append((nz, nx, ny, nmin))
          visited[nz][nx][ny] = True

  if not escaped:
    print('Trapped!')