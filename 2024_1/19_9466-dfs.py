# 9466 텀 프로젝트 DFS
import sys
sys.setrecursionlimit(9999999) # 재귀 제한 해제
input = sys.stdin.readline

def dfs(x):
  global ans
  visited[x] = True
  cycle.append(x) # 사이클 만들어지는 팀 확인 목적

  if visited[arr[x]]: # 추가로 사이클 만들어지는 곳 있는지 확인
    if arr[x] in cycle:
      ans += cycle[cycle.index(arr[x]):] # 사이클이 만들어지는 구간부터 팀 결성
    return
  else:
    dfs(arr[x])

for _ in range(int(input().rstrip())):
  N = int(input().rstrip())
  arr = [0] + list(map(int, input().rstrip().split())) # 학생 수 인덱스 : 1부터
  visited = [True] + [False] * N
  ans = []

  for i in range(1, N+1):
    if not visited[i]:
      cycle = [] # 2번째 조건(s1 -> s2, s2 -> s3, sr-1 -> sr, sr -> s1)
      dfs(i) # 방문하지 않는 노드
  
  print(N - len(ans))