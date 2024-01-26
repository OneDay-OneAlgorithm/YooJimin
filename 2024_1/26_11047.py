# 11047. 동전 0
# 그리디
N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

cnt = 0 

for i in reversed(range(N)):
    cnt += K//coin[i]
    K = K%coin[i]

print(cnt)
