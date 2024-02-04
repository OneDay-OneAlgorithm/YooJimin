# 2607 비슷한 단어
# 시작 시간 - 16:37
# 1차 풀이 종료 시간 - 16:51
# ---------------------------------------------
# < 1차 접근 >
# 두 개의 단어가 같은 종류의 문자로 이루어져 있음
# 같은 문자는 같은 개수 만큼 있음

import sys
input = sys.stdin.readline

N = int(input())
target = list(input())
ans = 0

for _ in range(N-1):
  compare = target[:] 
  word = input()
  cnt = 0
  for w in word:
    if w in compare:
      compare.remove(w)
    else:
      cnt += 1
  if cnt < 2 and len(compare) < 2:
    ans += 1

print(ans)