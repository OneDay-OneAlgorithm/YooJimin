# 1927 최소 힙
# 시작 시간 - 10:10
# 1차 풀이 종료 시간 - 10:24(정답)
# ---------------------------------------------
# < 1차 접근 >
# 최소 힙 사용
import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
hq = []
for _ in range(N):
  cmd = int(input().rstrip())
  if cmd == 0:
    if hq:
      print(heapq.heappop(hq))
    else:
      print(0)
  else:
    heapq.heappush(hq, cmd)