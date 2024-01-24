# 1992 쿼드트리
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
ans = []

def dfs(x, y, n):
  check = arr[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if arr[i][j] != check:
        ans.append('(')
        dfs(x, y, n // 2)
        dfs(x, y + (n//2), n // 2)
        dfs(x + (n // 2), y, n // 2)
        dfs(x + (n // 2), y + (n // 2), n // 2)
        ans.append(')')
        return

  ans.append(check)


dfs(0, 0, N)
print(*ans, sep='')