import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:(x[0], x[1]))

room = []
heapq.heappush(room, arr[0][1]) # 회의 종료 시간 넣어두기

for i in range(1, N):
  if arr[i][0] < room[0]: # 현재 회의가 끝나는 시간보다 다음 회의 시작 시간이 빠른 경우
    heapq.heappush(room, arr[i][1]) # 새로운 회의실 생성
  else: # 현재 회의실에서 이어서 회의가 가능하면
    heapq.heappop(room) # 새로운 회의로 시간 변경 위해 heappop()
    heapq.heappush(room, arr[i][1]) # 새로운 회의 넣기

print(len(room))
