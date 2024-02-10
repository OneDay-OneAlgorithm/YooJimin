# DP - 개미전사
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

# 앞서 계산된 결과를 저장하기 위해 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(보텀업)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, N):
  d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[N-1])