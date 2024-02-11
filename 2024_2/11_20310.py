# 20310 타노스
# 시작 시간 - 21:02
# 1차 풀이 종료 시간 - 21:14 (25점)
# 2차 풀이 종료 시간 - 21:21 (정답)
# ---------------------------------------------
# S가 포함하는 0의 개수와 1의 개수 모두 짝수
# S를 구성하는 문자 중 절반의 0과 절반의 1을 제거해 새로운 문자 S' 만듦
# S'로 가능한 문자열 중 사전순으로 가장 빠른 것

# S의 길이는 4의 배수
# S의 홀수번째 문자는 1, 짝수번째 문자 0

# < 1차 접근 >
# 그리디 -> 개수 나눠서

import sys
input = sys.stdin.readline

S = list(input().rstrip())
zero_cnt, one_cnt = S.count('0') // 2, S.count('1') // 2

for _ in range(zero_cnt):
  S.pop(-S[::-1].index('0') - 1)

for _ in range(one_cnt):
  S.pop(S.index('1'))

print(''.join(S))