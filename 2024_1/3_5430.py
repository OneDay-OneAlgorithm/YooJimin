import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
  cmd = input().rstrip()
  n = int(input())
  reverse_cnt = 0
  is_valid = True

  arr = sys.stdin.readline().rstrip()[1: - 1].split(',')
  dq = deque(arr)
  if n == 0:
    dq = []

  for c in cmd:
    if c == 'R':
      reverse_cnt += 1
    if c == 'D':
      if dq:
        if reverse_cnt % 2 == 0:
          dq.popleft()
        else:
          dq.pop()
      else:
        is_valid = False

  if is_valid:
    if reverse_cnt % 2 != 0:
      dq.reverse()
    ans = ','.join(dq)
    print(f'[{ans}]')
  else:
    print('error')