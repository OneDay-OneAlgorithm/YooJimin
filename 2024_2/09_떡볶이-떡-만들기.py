# 이진탐색 - 떡볶이 떡 만들기
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

start, end = 0, max(arr)

# 이진탐색
res = 0
while start <= end:
  total = 0
  mid = (start + end) // 2

  for i in arr: 
    if i > mid: # 잘랐을 때 떡 길이 계산
      total += i - mid
  
  if total < M: # 떡의 양이 부족한 경우 더 많이 자름(왼쪽 부분 탐색)
    end = mid - 1
  else: # 떡의 양이 충분한 경우 덜 자름(오른쪽 부분 탐색)
    res = mid # 최대한 덜 자를 경우를 정답으로
    start = mid + 1

print(res)