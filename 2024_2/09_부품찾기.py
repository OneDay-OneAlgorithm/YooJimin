# 이진탐색 - 부품찾기
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
find_arr = list(map(int, input().rstrip().split()))

arr.sort()
find_arr.sort()

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
      return 'yes'
    
    elif arr[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1
  return 'no'

for i in range(len(find_arr)):
  print(binary_search(arr, find_arr[i], 0, N-1), end= ' ')