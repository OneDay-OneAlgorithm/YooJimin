# 11729 하노이의 탑 이동 순서

import sys
input = sys.stdin.readline
N = int(input().rstrip())

def hanoi(N, start, end):
  if N == 1:
    print(start, end)
    return

  else:
    hanoi(N-1, start, 6 - start - end)
    print(start, end)
    hanoi(N-1, 6 - start - end, end)

sum = 2 ** N - 1
print(sum)

hanoi(N, 1, 3)

# arr = [[] for _ in range(3)] # 하노이 1, 2, 3번탑 초기화
# arr[0].append(list(i+1 for i in range(N))) # 첫번째 탑에 데이터 넣기

