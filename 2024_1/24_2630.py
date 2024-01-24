# 2630 색종이 만들기
import sys
input = sys.stdin.readline
ans = [0, 0] # white, blue

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

def dfs(x, y, n):
  check = arr[x][y] # 숫자 체크를 위한 값
  for i in range(x, x+n):
    for j in range(y, y+n):
      if arr[i][j] != check: 
        for k in range(2):
          for l in range(2):
            dfs(x + (k*n) // 2, y + (l*n) // 2, n // 2)
        return

  if check == 0: # 하얀색으로 칠해진 칸
    ans[0] += 1
  elif check == 1: # 파란색으로 칠해진 칸
    ans[1] += 1

dfs(0, 0, N)
print(*ans, sep='\n')