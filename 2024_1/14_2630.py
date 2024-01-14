# 바킹독 재귀 2630 https://www.acmicpc.net/problem/2630
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white_cnt, blue_cnt = 0, 0

def dfs(x, y, n):
  global white_cnt, blue_cnt
  equal_check = arr[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if equal_check != arr[i][j]:
        dfs(x, y, n//2)
        dfs(x, y+n//2, n//2)
        dfs(x+n//2, y, n//2)
        dfs(x+n//2, y+n//2, n//2)
        return

  if equal_check == 0:
    white_cnt += 1
  elif equal_check == 1:
    blue_cnt += 1

dfs(0, 0, N)
print(f'{white_cnt}\n{blue_cnt}')
