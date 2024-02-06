# 구현 - 게임 개발
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
# 방문한 위치를 저장하기 위한 맵을 생성해 0으로 초기화
d = [[False]*M for _ in range(N)]

# x, y, direction: (A, B), d: 바라보는 방향
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
x, y, direction = map(int, input().rstrip().split())
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
d[x][y] = True # 현재 좌표 방문 처리

# 맵 정보 입력
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 왼쪽으로 회전하는 함수
def turn_left():
  global direction
  direction -= 1 # 왼쪽으로 회전
  if direction == -1:
    direction = 3 # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽

# 시뮬레이션
cnt = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx, ny = x + dx[direction], y + dy[direction]
  
  # 회전한 후 정면에 방문하지 않은 곳이 존재하는 경우
  if d[nx][ny] == 0 and arr[nx][ny] == 0:
    d[nx][ny] = True
    x, y = nx, ny
    cnt += 1
    turn_time = 0
    continue
  
  # 회전한 이후 정면에 방문하지 않은 곳 없거나 바다인 경우
  else:
    turn_time += 1
  
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx, ny = x - dx[direction], y - dy[direction]
    # 뒤로 갈 수 있는 경우 이동
    if arr[nx][ny] == 0: # 육지
      x, y = nx, ny
    else: # 바다
      break
    turn_time = 0

print(cnt)