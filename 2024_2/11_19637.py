# 19637 IF문 좀 대신 써줘
# 시작 시간 - 21:23
# 1차 풀이 종료 시간 - 21:30 (시간초과)
# 2차 풀이 종료 시간 - 21:36 (정답)
# ---------------------------------------------
# < 1차 접근 >
# 무지성으로 구현을 해버렸으나.. -> 이분탐색으로 접근해야 함

# < 2차 접근 >
# 이분탐색으로 bisect_left 값을 찾아 tag에서 해당 칭호 찾기

import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # N: 칭호의 개수, M: 칭호를 출력해야 하는 캐릭터 개수
tag, power = [], []

for _ in range(N):
  a, b = input().rstrip().split()
  tag.append(a)
  power.append(int(b))

for _ in range(M):
  print(tag[bisect_left(power, int(input().rstrip()))])
