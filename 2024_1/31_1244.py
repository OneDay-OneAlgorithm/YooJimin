# 1244 스위치 켜고 끄기

import sys
input = sys.stdin.readline

def change(num):
    if arr[num] == 0:
        arr[num] = 1
    else:
        arr[num] = 0
    return

N = int(input().rstrip())
arr = [-1] + list(map(int, input().rstrip().split()))
SN = int(input().rstrip())
for _ in range(SN):
    sex, num = map(int, input().rstrip().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if arr[num + k] == arr[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(arr[i], end = " ")
    if i % 20 == 0 :
        print()
