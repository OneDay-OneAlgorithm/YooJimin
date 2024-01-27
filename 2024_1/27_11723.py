# 11723 집합
# 시작 시간 - 12:47
# 1차 풀이 종료 시간 - 12:57
# ---------------------------------------------
# Set : add / discard
import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input().rstrip())):
  cmd = input().rstrip().split()
  if len(cmd) == 1:
    if cmd[0] == 'all':
      S = set([i+1 for i in range(20)])
    else:
      S = set()

  else:
    cmd, x = cmd[0], int(cmd[1])
    if cmd == 'add':
      S.add(x)
    elif cmd == 'check':
      print(1 if x in S else 0)
    elif cmd == 'remove':
      if x in S:
        S.discard(x)
    elif cmd == 'toggle':
      if x in S:
        S.discard(x)
      else:
        S.add(x)