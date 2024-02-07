# DFS - 음료수 얼려 먹기
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  
  # 현재 노드를 아직 방문하지 않은 경우
  if arr[x][y] == 0:
    arr[x][y] = 1 # 방문 처리
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  
  return False

ans = 0
for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      ans += 1

print(ans)