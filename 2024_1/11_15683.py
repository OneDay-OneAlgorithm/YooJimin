# 15683 감시
import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = []
cctv = deque()

dir = {
  1: [[0], [1], [2], [3]], # 1번 cctv : 4가지
  2: [[0, 2], [1, 3]], # 2번 cctv : 2가지
  3: [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번 cctv : 4가지
  4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번 cctv : 4가지 
  5: [[0, 1, 2, 3]], # 5번 cctv : 1가지
}

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 동 서 남 북 순서

for i in range(N):
  data = list(map(int, input().rstrip().split()))
  arr.append(data)
  for j in range(M):
    if data[j] in [1, 2, 3, 4, 5]: # cctv를 포함하는 경우
      cctv.append((data[j], i, j)) # cctv의 종류, 좌표 추가

# cctv가 바라보는 방향에 따른 감시 영역 체크 함수
def fill(arr, index, x, y):
  for i in index:
    nx, ny = x, y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        break
      if arr[nx][ny] == 6:
        break
      elif arr[nx][ny] == 0:
        arr[nx][ny] = 7 # 감시가 가능한 곳을 7으로 변환

# dfs함수
def dfs(depth, arr):
  global min_val
  if depth == len(cctv):
    cnt = 0
    for i in range(N):
      cnt += arr[i].count(0)
    min_val = min(min_val, cnt)
    return

  tmp = copy.deepcopy(arr)
  cctv_num, x, y = cctv[depth]
  for i in dir[cctv_num]:
    fill(tmp, i, x, y)
    dfs(depth+1, tmp)
    tmp = copy.deepcopy(arr)

min_val = int(99999)
dfs(0, arr)
print(min_val)