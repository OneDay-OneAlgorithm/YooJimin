import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []
sum = 0
multi = 1

for i in range(len(arr)):
  if arr[i] == '(':
    stack.append(arr[i])
    multi *= 2
  elif arr[i] == '[':
    stack.append(arr[i])
    multi *= 3
  elif arr[i] == ')':
    if not stack or stack[-1] == '[':
      sum = 0
      break
    if arr[i-1] == '(':
      sum += multi
    stack.pop()
    multi //= 2
  elif arr[i] == ']':
    if not stack or stack[-1] == '(':
      sum = 0
      break
    if arr[i-1] == '[':
      sum += multi
    stack.pop()
    multi //= 3
print(0 if stack else sum)
