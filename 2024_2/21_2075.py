import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
hq = []

for i in range(N):
  num_list = list(map(int, input().rstrip().split()))
  if not hq:
    for num in num_list:
      heapq.heappush(hq, num) # 최소힙으로 데이터 채움
  else:
    for num in num_list: # hq에 값이 있는 경우 hq의 길이를 N으로 유지시키는 작업
      if hq[0] < num: # 최소값보다 순회 중인 리스트 내부 값이 큰 경우
        heapq.heappop(hq) # hq에서 hq의 최소값 pop
        heapq.heappush(hq, num) # 순회 중인 리스트 내부 값 push

print(hq[0])