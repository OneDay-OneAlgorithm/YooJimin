# 오큰수 17298 https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
  while stack and arr[stack[-1]] < arr[i]:
    ans[stack.pop()] = arr[i]
  stack.append(i)

print(*ans)
