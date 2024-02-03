# 19941 햄버거 분배
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
arr = list(input().rstrip())
ans = 0

for i in range(N):
  if arr[i] == 'P':
    # i - K ~ i + K + 1
    for j in range(max(i - K, 0), min(i + K + 1, N)): 
      if arr[j] == 'H':
        arr[j] = 0
        ans += 1
        break

print(ans)
