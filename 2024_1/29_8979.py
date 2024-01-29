# 8979 올림픽

N, K = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(N)] # 0 : 국가 정수, 1~3: 메달
score.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True) # 메달 개수에 따라 내림차순 정렬(lambda 조건 통해 메달 개수 같을 경우 다음으로)
selected_nation = [score[i][0] for i in range(N)].index(K) # score[i][0]: 국가 나타내는 정수. 국가명이 K와 일치하는 인덱스 찾아서 저장
# print(score, selected_nation)

for i in range(N): # 동점 국가 확인
  if score[selected_nation][1:] == score[i][1:]: # 일치하는 다른 국가 없을 경우
    print(i+1)
    break