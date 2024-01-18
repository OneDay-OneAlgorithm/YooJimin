# 4179 불!
import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().rstrip().split())

arr = []
jihun_pos = [] # 지훈 현위치
fire_pos = [] # 불 위치

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs():
  while dq:
    x, y, case = dq.popleft()
    if case == 'J' and (x == 0 or y == 0 or x == R - 1 or y == C - 1): # 탈출이 가능한 조건
      if arr[x][y] == '#': # 건널 수 없는 길인 경우
        continue
      return arr[x][y] + 1 # +1의 값 리턴(탈출 조건을 충족했을 때 밖으로 나오기 때문)

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < R and 0 <= ny < C:
        if arr[nx][ny] != '#' and case == 'F': # 다음 (nx,ny)가 벽이 아니고, 불인 경우 (벽일 경우 통과 X)
          arr[nx][ny] = '#'
          dq.append((nx, ny, 'F')) # (nx, ny)를 불으로 저장
        elif arr[nx][ny] == '.' and case == 'J' and arr[x][y] != '#': # 다음 (nx, ny)가 이동 가능한 경로인 경우
          arr[nx][ny] = arr[x][y] + 1 # 이동 경로 + 1
          dq.append((nx, ny, 'J')) # (nx, ny)를 지훈 경로로 저장
  
  return 'IMPOSSIBLE'

for i in range(R):
  tmp = list(input().rstrip())
  for j in range(C):
    if tmp[j] == 'J': # 지훈 위치가 있는 경우
      jihun_pos.append((i, j)) # 지훈 위치 추가
    elif tmp[j] == 'F': # 불 위치가 있는 경우
      fire_pos.append((i, j)) # 불 위치 추가

  arr.append(tmp) # 배열에 입력 값 저장

dq = deque()
dq.append((jihun_pos[0][0], jihun_pos[0][1], 'J')) # 지훈 위치 x값, y값, 지훈 이동
arr[jihun_pos[0][0]][jihun_pos[0][1]] = 0 # 덱에 넣었으니 값 0으로 변경

if len(fire_pos) != 0: # 불이 있다면
  for i, j in fire_pos:
    dq.append((i, j, 'F')) # 불 위치 x값, y값, 불 표시
    arr[i][j] = '#'

print(bfs())