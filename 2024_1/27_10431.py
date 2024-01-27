# 10431 줄세우기
# 시작 시간 - 15:41
# 1차 풀이 종료 시간 - 15:56
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
  arr = list(map(int, input().rstrip().split()))
  cnt = 0 # 뒤로 가는 횟수
  for i in range(1, len(arr) - 1): # 버블소트
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]: # 지금 순회하는 인덱스의 값보다 앞에 더 큰 값이 있는 경우
        arr[i], arr[j] = arr[j], arr[i] 
        cnt += 1 

  print(arr[0], cnt)