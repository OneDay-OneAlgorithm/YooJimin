# 6236 용돈 관리

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
budget = [int(input()) for _ in range(N)]
left,right = min(budget), sum(budget)

while left <= right:
    mid = (left+right)//2
    curr = mid
    draw = 1

    for i in budget:
        if curr < i:
            curr = mid
            draw+=1
        curr -= i
    
    if draw > M or mid < max(budget):
        left = mid+1
    else:
        right = mid-1
        k = mid
print(k)