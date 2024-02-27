import sys
input = sys.stdin.readline

while True:
  graph = list(map(int, input().rstrip().split()))

  # 0이 입력되면 반복문 종료
  if graph[0] == 0:
    break

  # 스택과 최대 직사각형 넓이를 저장할 변수 초기화
  stack = []
  max_result = 0

  for i, height in enumerate(graph):
    if i == 0:  # 첫 번째 i는 막대기의 개수를 의미하므로 pass
      continue

    # 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 작은 경우
    if stack and stack[-1][1] > height:
      while stack:  # 스택에서 빼내며 최대 직사각형 넓이 계산
        stack_i, stack_height = stack.pop()
        width_start = 1

        if stack:
          width_start = stack[-1][0]+1

        result = (i - width_start) * stack_height
        max_result = max(result, max_result) # 최대값 갱신

        # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
        if not stack or stack[-1][1] <= height:
          break

    # 스택이 비어 있거나 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 크거나 같으면
    if not stack or stack[-1][1] <= height:
        stack.append((i, height))  # 스택에 현재 막대기 추가

  # 반복이 종료되고, 스택에 남은 막대기가 있다면
  while stack:
      stack_i, stack_height = stack.pop()
      width_start = 1

      if stack:
          width_start = stack[-1][0]+1

      result = (graph[0]+1 - width_start) * stack_height
      max_result = max(result, max_result) # 최대값 갱신

  print(max_result)