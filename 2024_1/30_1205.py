# 1205 등수 구하기

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, Taesu, P = map(int, input().rstrip().split())
arr = []

if N > 0:
  arr = list(map(int, input().rstrip().split()))
arr.sort()

if len(arr) < P: # 랭킹 리스트가 꽉 차지 않은 경우
  idx = bisect_left(arr, Taesu)
  arr.insert(idx, Taesu)
  score = len(arr) - bisect_right(arr, Taesu) + 1
  print(score)

elif min(arr) < Taesu: # 랭킹 리스트가 꽉 찼지만, 새 점수가 이전 점수보다 더 좋은 경우
  arr[arr.index(min(arr))] = Taesu
  score = len(arr) - bisect_right(arr, Taesu) + 1
  print(score)
else:
  print(-1)
