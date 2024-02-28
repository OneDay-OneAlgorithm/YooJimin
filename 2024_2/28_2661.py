import sys
N = int(input())
ans = []

def check(arr):
  arr_len = len(arr)
  for part_len in range(1, arr_len // 2 + 1):
    for part_start in range(part_len, arr_len - part_len + 1):
      if arr[part_start - part_len : part_start] == arr[part_start : part_start + part_len]:
        return False
  return True

def dfs(length, arr):
  if length == N: # 길이가 N이 되면
    print(''.join(list(map(str, arr)))) # 수열 출력
    sys.exit() # 종료

  arr.append(1) #  1 추가
  for i in range(1, 4): # 1 ~ 3 순회
    arr.pop()
    arr.append(i)
    if check(arr):
      if not dfs(length + 1, arr):
        continue
  else:
    arr.pop()
    return False

dfs(1, [1])