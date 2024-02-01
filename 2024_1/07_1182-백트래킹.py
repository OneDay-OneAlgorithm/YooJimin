# 1182 부분수열의 합 - 백트래킹
import sys
input = sys.stdin.readline

def dfs(idx, total):
  global cnt
  if idx >= N:
    return
  total += arr[idx]
  if total == S:
    cnt += 1
  dfs(idx + 1, total - arr[idx])
  dfs(idx + 1, total)

N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
cnt = 0

dfs(0, 0)
print(cnt)