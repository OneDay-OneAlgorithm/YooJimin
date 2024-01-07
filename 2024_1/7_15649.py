# 15649 N과 M (1)
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [i+1 for i in range(N)]
ans = list(permutations(arr, M))

for i in range(len(ans)):
  print(*ans[i])