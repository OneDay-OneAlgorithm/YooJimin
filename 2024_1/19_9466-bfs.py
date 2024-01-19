# 9466 텀 프로젝트
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
  n = int(input().rstrip())
  arr = [0] + list(map(int, input().rstrip().split()))
  candidates = set(range(1, n+1)) # 후보 set -> 방문 시마다 set에서 제거
  ans = n

  while candidates:
    candi = candidates.pop()
    cnt = 1
    d = defaultdict(int) # 정수형 defaultdict 생성

    while True:
      d[candi] = cnt
      cnt += 1
      if arr[candi] in candidates:
        candidates.remove(arr[candi])
        candi = arr[candi]
      else:
        if d[arr[candi]] != 0:
          ans -= cnt - d[arr[candi]]
        break

  print(ans)