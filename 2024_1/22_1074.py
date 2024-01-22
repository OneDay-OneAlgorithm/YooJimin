# 1074 z
import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

def z(N, r, c):
  if N == 0:
    return 0
  # 좌표값 r, c가 2배 -> 값이 4의 배수로 확장
  return 2 * (r % 2) + (c % 2) + 4 * z(N-1, int(r / 2), int(c / 2))

print(z(N, r, c)) 
