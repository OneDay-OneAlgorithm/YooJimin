# 3758 KCPC

# < 1차 접근 >
# 정렬 문제
# 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다. 
# 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다. 

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
  # n: 팀 개수, k: 문제 개수, t: 팀 ID, m: 로그 엔트리 개수 m
  n, k, t, m = map(int, input().rstrip().split()) 
  arr = [[0] * k for _ in range(n)]
  cnt, time = [0] * n, [0] * n # cnt: 제출한 횟수, time: 제출한 시간

  # i: 팀 ID, j: 문제 번호, s: 획득한 점수
  for test in range(m): # 로그 엔트리 개수만큼 반복
    i, j, s = map(int, input().rstrip().split())
    arr[i-1][j-1] = max(arr[i-1][j-1], s)
    time[i-1] = test
    cnt[i-1] += 1
    # print(f'arr: {arr}, time: {time}, cnt: {cnt}')
  new = []
  for idx in range(len(arr)):
    new.append([sum(arr[idx]), cnt[idx], time[idx], idx])
    # print(f'new: {new}')
  new.sort(key=lambda x:(-x[0], x[1], x[2])) # 최종 점수, 풀이 제출 횟수, 제출 시간
  for idx in range(len(new)):
    if new[idx][3] == t - 1:
      print(idx + 1)
      break
