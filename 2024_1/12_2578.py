board = [] # 내 빙고
for _ in range(5):
    board.append(list(map(int,input().split())))

people = [] # 사회자가 부르는 순서
for _ in range(5):
    people.append(list(map(int,input().split())))

visited = [[False]*5 for _ in range(5)] # 빙고 여부를 판단하는 그래프

def garo(visited):  # 가로 빙고만 확인
    cnt = 0
    for col in visited:
        if sum(col) == 5:
            cnt += 1
    return cnt


def sero(visited): # 세로 빙고만 확인
    cnt = 0
    temp = list(map(list,zip(*visited)))[::-1] # zip을 사용한 반시계 방향 회전
    for col in temp: # 이를 통해 가로 빙고 확인할 때처럼 쉽게 확인 가능
        if sum(col) == 5:
            cnt += 1
    return cnt


def cross_left(visited): # 왼쪽 대각선 체크 (북서 -> 남동)
    cnt = 0
    temp = 0
    for idx in range(5):
        temp += visited[idx][idx]
    if temp == 5:
        cnt = 1
    return cnt


def cross_right(visited): # 오른쪽 대각선 체크 (북동 -> 남서)
    cnt = 0
    temp = 0
    for idx in range(5):
        temp += visited[idx][4-idx]
    if temp == 5:
        cnt = 1
    return cnt


def bingo(check,ccnt): # 빙고 확인하는 함수들을 호출하는 곳 + visited 처리
    for col in range(5):
        for row in range(5):       
            if check == board[col][row]:
                visited[col][row] = True
                cnt1 = garo(visited)
                cnt2 = sero(visited)
                cnt3 = cross_left(visited)
                cnt4 = cross_right(visited)
                if cnt1+cnt2+cnt3+cnt4 >= 3:
                    print(ccnt)
                    exit()
                  
ccnt = 0 # 사회자가 몇번째 숫자를 부르는지 체크용
for col in range(5):
    for row in range(5):
        ccnt += 1
        check = people[col][row]
        bingo(check,ccnt)
