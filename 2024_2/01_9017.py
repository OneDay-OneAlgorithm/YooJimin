# 9017 크로스 컨트리

import sys
from collections import Counter
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
  N = int(input().rstrip())
  arr = list(map(int, input().rstrip().split()))
  
  counter = Counter(arr)
  score = {}
  cnt = 0

  for i in range(N):
    if counter[arr[i]] < 6:
      cnt += 1
      continue

    if arr[i] in score:
      score[arr[i]].append(i - cnt + 1)
    
    else:
      score[arr[i]] = [i - cnt + 1]

  print(sorted(score, key=lambda x:(sum(score[x][:4]), score[x][4]))[0])