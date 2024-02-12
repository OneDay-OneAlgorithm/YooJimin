# 22233 가희와 키워드

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

memo, answer = [], []

for _ in range(N):
  memo.append(input().rstrip())
memo = set(memo)
for _ in range(M):
  post = list(input().rstrip().split(','))
  memo -= set(post)
  print(len(memo))