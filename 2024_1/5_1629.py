# 1629 곱셈
import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

def multi(a, b):
  if b == 1: # b의 값이 1이 될 때까지 재귀
    return a % C
  else:
    tmp = multi(a, b//2)
    if b % 2 == 0:
      return (tmp * tmp) % C # b의 값이 짝수인 경우
    else:
      return (tmp * tmp * a) % C # b의 값이 홀수인 경우

print(multi(A, B))

# 시간 초과난 코드
# A, B, C = map(int, input().rstrip().split())
# print((A ** B) % C)