import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
  cmd = input().rstrip()
  stack = []
  for i in range(len(cmd)):
    if stack and stack[-1] == cmd[i]: 
      stack.pop()
    else:
      stack.append(cmd[i])
  if not stack:
    cnt += 1

print(cnt)
