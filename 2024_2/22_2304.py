# 2304 창고 다각형

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)] # arr[x][0]: 기둥 왼쪽면의 위치, arr[x][1]: 높이
ans = 0
max_height = 0

arr.sort(key=lambda x: x[0]) # x축 기준 arr 정렬
for i in range(len(arr)):
  if arr[i][1] > ans:
    ans = arr[i][1]
    idx = i

# 초기 높이를 첫번째 기둥의 높이로 초기화
height = arr[0][1]

# 최대 높이를 만나기 전까지 돌며 다음 기둥이 현재보다 높은 경우
for i in range(idx): # 가장 높은 기둥이 있는 인덱스까지(가장 높은 기둥 인덱스의 왼쪽)
  if height < arr[i+1][1]:
    ans += height * (arr[i+1][0] - arr[i][0])
    height = arr[i+1][1]
  # 아닌 경우 현재 면적만 더해줌
  else:
    ans += height * (arr[i+1][0] - arr[i][0])

# 뒤에서부터도 진행
height = arr[-1][1]

for i in range(N-1, idx, -1): # 가장 높은 기둥이 있는 인덱스까지 거꾸로(가장 높은 기둥 인덱스의 오른쪽)
  if height < arr[i-1][1]:
    ans += height * (arr[i][0] - arr[i-1][0])
    height = arr[i-1][1]
  else: # 아닌 경우 현재 면적만을 더함
    ans += height * (arr[i][0] - arr[i-1][0])

print(ans)