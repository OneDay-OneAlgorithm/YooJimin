# 15649 N과 M(1) - 백트래킹
import sys
input = sys.stdin.readline

def dfs():
  if len(ans) == M:
    print(' '.join(map(str, ans)))
    return
  
  for i in range(1, N+1):
    if visited[i]:
      continue
    else:
      visited[i] = True
      ans.append(i)

      dfs()

      ans.pop()
      visited[i] = False

N, M = map(int, input().rstrip().split())
ans = []
visited = [False] * (N+1)

dfs()