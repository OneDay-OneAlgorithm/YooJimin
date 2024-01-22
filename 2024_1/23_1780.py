# 1780 종이의 개수
import sys
sys.setrecursionlimit(9999999)
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
ans = [0, 0, 0] # -1, 0, 1

def dfs(x, y, n):
  check = arr[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if arr[i][j] != check:
        for k in range(3):
          for l in range(3):
            dfs(x + (k * n) // 3, y + (l * n) // 3, n // 3)
        return

  if check == -1:
    ans[0] += 1
  elif check == 0:
    ans[1] += 1
  elif check == 1:
    ans[2] += 1

dfs(0, 0, N)
print(*ans, end='\n')