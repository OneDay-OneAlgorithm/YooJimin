# 5014 스타트링크
import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().rstrip().split())
arr = [[] for _ in range(F + 1)] # 정점 개수(층 수)
dist = [0] * (F + 1) # 횟수 저장

dq = deque()
dq.append(S) # 현재 위치를 덱에 추가

while dq:
  curr = dq.popleft()

  if curr == G : # 도착지점인 경우
    print(dist[curr])
    break

  for next in (curr + U, curr - D): # curr으로부터 +U or -D 
    if next == curr:
      continue # U가 D이거나 0인 경우

    if 1 <= next <= F and not dist[next]:
      dist[next] = dist[curr] + 1 # 방문처리 후 횟수 + 1
      dq.append(next)

else:
  print("use the stairs")