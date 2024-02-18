import sys
input = sys.stdin.readline

# N : 다음 줄로 주어질 정수의 개수
N = int(input())
# A : N개의 정수 (targets의 포함 여부의 기준이 될 배열)
A = list(map(int, input().split()))
# 이분 탐색의 조건 : 정렬된 배열로 시작
A.sort()

# M : 다음 줄로 주어질 정수의 개수
M = int(input())
# targets : A에 포함되어 있는지 확인하기 위한 배열
targets = list(map(int, input().split()))

def binary_search(target):
  # left와 right 초기화
  left = 0
  right = N - 1

  while left <= right:
    # 중간 값 설정
    mid = (left + right) // 2
    # target의 값이 중간 값과 같은 case
    if A[mid] == target:
      return True
    # target의 값이 중간 값보다 작은 case (target가 mid보다 왼쪽에 위치)
    if target < A[mid]:
      right = mid-1
    # target의 값이 중간 값보다 큰 case (target이 mid보다 오른쪽에 위치)
    elif target > A[mid]:
      left = mid + 1

# M개의 원소 순회
for i in range(M):
  # targets[i]를 순회하며 Binary_search
  if binary_search(targets[i]):
    print(1)
  else:
    print(0)
