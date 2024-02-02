# 1515 수 이어 쓰기
import sys
input = sys.stdin.readline

N = input().rstrip()
ans = 0 # 최솟값
while True:
  ans += 1
  num = str(ans) # 각 자릿수 비교를 위해 문자열로 변환
  while len(num) > 0 and len(N) > 0:
    # print(f'ans: {ans}, num: {num}, N: {N}')
    if num[0] == N[0]:
      N = N[1:]
      # print(f'in if - N: {N}')
    num = num[1:]
  if N == '':
    print(ans)
    break