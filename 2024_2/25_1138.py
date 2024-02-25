N = int(input())
H = list(map(int, input().split()))
ans = [0] * N
for i in range(1, N+1):
    T = H[i-1]
    cnt = 0
    
    for j in range(N):
        if cnt == T and ans[j] == 0:
            ans[j] = i
            break
        elif ans[j] == 0:
            cnt += 1
print(*ans)