# 7568 덩치
# 시작 시간 - 15:23
# 1차 풀이 종료 시간 - 15:40
# ---------------------------------------------
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr.sort(key = lambda x : (x[0] , x[1]), reverse=True)
grade = []
# print(arr)
for i in range(N):
  cnt = 0
  for j in range(N):
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: # 키와 몸무게가 모두 더 많이 나가는 경우
      cnt += 1
  grade.append(cnt + 1)

print(*grade)