# 1182 부분수열의 합
import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
cnt = 0

for i in range(len(arr) + 1):
  candidate = list(combinations(arr, i+1))

  for candi in candidate:
    if sum(candi) == S:
      cnt += 1

print(cnt)