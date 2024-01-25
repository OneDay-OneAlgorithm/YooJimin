# 23971 ZOAC 4
import sys, math
input = sys.stdin.readline

H, W, N, M = map(int, input().rstrip().split())
row = math.ceil(W / (M + 1))
col = math.ceil(H / (N + 1))

print(row * col)