# 17266 어두운 굴다리

import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 굴다리 길이
M = int(input().rstrip()) # 가로등 개수
pos = list(map(int, input().rstrip().split())) # 가로등의 위치 x(M개의 값)

max_gap = max(pos[0], N - pos[-1]) * 2 # 좌우 포함 가로등이 밝혀야 하는 최대 거리
for i in range(1, M):
  max_gap = max(max_gap, pos[i] - pos[i-1])

light_height = (max_gap + 1) // 2 # 최소 높이값 계산
print(light_height)