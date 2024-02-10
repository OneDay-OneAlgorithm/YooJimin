# DP - 효율적인 화폐 구성
# 그리디에서의 거스름돈 문제와 동일 -> 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점이 다름
# -> DP를 이용해야 하는 문제

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(N)]

# 한 번 계산된 결과 저장을 위한 DP 테이블 초기화
d = [10001] * (M+1)

# DP (보텀업)
d[0] = 0
for i in range(N):
  for j in range(arr[i], M+1):
    if d[j - arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j-arr[i]] + 1)

# 계산된 결과 출력
if d[M] == 10001: # M원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[M])
