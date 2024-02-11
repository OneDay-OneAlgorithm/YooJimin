# 20310 타노스
# 시작 시간 - 21:02
# 1차 풀이 종료 시간 - 21:14 (25점)
# ---------------------------------------------
# S가 포함하는 0의 개수와 1의 개수 모두 짝수
# S를 구성하는 문자 중 절반의 0과 절반의 1을 제거해 새로운 문자 S' 만듦
# S'로 가능한 문자열 중 사전순으로 가장 빠른 것

# S의 길이는 4의 배수
# S의 홀수번째 문자는 1, 짝수번째 문자 0

# < 1차 접근 >
# 그리디 -> 개수 나눠서

import sys
from collections import Counter
input = sys.stdin.readline

S = input().rstrip()
counter = Counter(S)
zero_cnt, one_cnt = counter['0'], counter['1']
arr = [0] * (zero_cnt//2) + [1] * (one_cnt//2)
print(*arr, sep='')