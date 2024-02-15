import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
total = int(input().rstrip())

start, end = 0, max(arr) # 최솟값과 최대값 설정
mid = (start + end) // 2
ans = 0

def is_possible(mid):
  return sum(min(cost, mid) for cost in arr) <= total

while start <= end:
  if is_possible(mid):
    start = mid + 1
    ans = mid
  else:
    end = mid - 1
  mid = (start + end) // 2

print(ans)