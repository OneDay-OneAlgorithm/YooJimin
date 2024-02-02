# 21921 블로그
import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
visitors = list(map(int, input().rstrip().split()))

if max(visitors) == 0: # 최대 방문자가 0인 경우
  print("SAD")

else:
  max_visitor = sum(visitors[0:X]) # 왼쪽부터 시작(슬라이딩 윈도우)
  value = max_visitor
  duration = 1
  for i in range(X, N):
    value -= visitors[i-X] # 왼쪽 한 칸 빼고
    value += visitors[i] # 오른쪽 한 칸 더하고
    if value > max_visitor: # 최댓값 갱신하고
      max_visitor = value
      duration = 1
    elif value == max_visitor: # 같은 값 또 나오면 반복횟수 갱신하고
      duration += 1
  
  print(max_visitor, duration, sep='\n')