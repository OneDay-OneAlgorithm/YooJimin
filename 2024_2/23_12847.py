import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

step = m
window = sum(arr[:step])
ans = window
for i in range(step, n):
    window += arr[i] - arr[i - step]
    ans = max(ans, window)

print(ans)
