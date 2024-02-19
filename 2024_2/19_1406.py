# 1406 에디터
# 1차 : 15:04
# ---------------------------------------------
import sys
input = sys.stdin.readline

left_stack, right_stack = list(input().rstrip()), []
M = int(input())

for _ in range(M):
  cmd = list(map(str, input().rstrip().split()))
  if cmd[0] == 'L' and left_stack:
    right_stack.append(left_stack.pop())
  if cmd[0] == 'D' and right_stack:
    left_stack.append(right_stack.pop())
  if cmd[0] == 'B' and left_stack:
    left_stack.pop()
  if cmd[0] == 'P':
    left_stack.append(cmd[1])

print(''.join(left_stack + list(reversed(right_stack))))