# 2292 벌집

N = int(input())
nums_pileup = 1 # 벌집의 개수, 1개부터 시작
cnt = 1 # 사이클이 도는 횟수, 반복하는 횟수
while N > nums_pileup:
  nums_pileup += 6 * cnt # 벌집이 6의 배수로 증가
  cnt += 1 # 반복문을 반복하는 횟수
  # print(nums_pileup, cnt)
print(cnt)