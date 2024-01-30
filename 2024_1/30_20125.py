# 20125 쿠키의 신체 측정

import sys
input = sys.stdin.readline

N = int(input().rstrip())
board = [list(map(str, input().rstrip())) for _ in range(N)]
head_flag = False
body_cnt = [0, 0, 0, 0, 0] # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리

for i in range(N):
  for j in range(N):
    if board[i][j] == '*' and not head_flag:
      head_flag = True
      heart = (i+2, j+1) # 심장 좌표
      break

for i in range(heart[1] - 1): # 왼쪽 팔
  if board[heart[0]-1][i] == '*': 
    body_cnt[0] += 1

for i in range(heart[1], N): # 오른쪽 팔
  if board[heart[0]-1][i] == '*': 
    body_cnt[1] += 1

line = 0 # 허리 끝부분 체크
for i in range(heart[0], N): # 허리
  if board[i][heart[1] - 1] == '*': 
    body_cnt[2] += 1
    line = i

for i in range(N-1, line, -1): # 왼쪽 다리
  if board[i][heart[1] - 2] == '*':
    body_cnt[3] += 1

for i in range(N-1, line, -1): # 오른쪽 다리
  if board[i][heart[1]] == '*':
    body_cnt[4] += 1

print(*heart)
print(*body_cnt)