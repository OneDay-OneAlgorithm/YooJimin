import sys

input = sys.stdin.readline

S = list(map(int, input().rstrip()))

zero_cnt = 0
one_cnt = 0

for i in range(len(S) - 1):
  if i == 0:
    if S[i] == 0:
      zero_cnt += 1
    elif S[i] == 1:
      one_cnt += 1
  if i == len(S) - 1:
    if S[i] == 0:
      zero_cnt += 1
    elif S[i] == 1:
      one_cnt += 1
  else:
    if S[i] != S[i + 1]:
      if S[i] == 0:
        one_cnt += 1
      elif S[i] == 1:
        zero_cnt += 1

print(min(zero_cnt, one_cnt))
