# 10026 적녹색약
import sys
sys.setrecursionlimit(1000000) # 재귀 제한 늘려줌
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0 # 적녹색약 X, 적녹색약 O
dx, dy = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y):
    #현재 색상 좌표 방문
    visited[x][y] = True
    current_color = matrix[x][y] # 현재 색상 값으로 갱신

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같은 경우
                if matrix[nx][ny] == current_color: 
                    dfs(nx,ny) # dfs에 넣고 재귀 돌리기

# 적녹색약이 아닌 사람
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표의 경우 dfs로
        if visited[i][j] == False:
            dfs(i,j)
            three_cnt += 1 # 개수 갱신

# 적녹색약인 사람 배열 초기화
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='R':
            matrix[i][j]='G' # R을 G로 통일
visited = [[False] * n for _ in range(n)] # 방문 여부 배열 초기화

# 적녹색약인 사람
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1 # 개수 갱신

print(three_cnt,two_cnt)