while True:
  stack = []
  arr = input()
  if arr == '.':
    break
  
  for i in arr:
    if i == '[' or i == '(':
      stack.append(i)
    elif i == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(']')
        break
    elif i == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(')')
        break

  print('no' if stack else 'yes')
