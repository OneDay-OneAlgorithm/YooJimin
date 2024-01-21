# 바킹독 정렬 11650 https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
  arr[i] = list(map(int, input().rstrip().split()))

arr.sort(key=lambda x: (x[0], x[1]))
for i in range(len(arr)):
  print(f'{arr[i][0]} {arr[i][1]}')
