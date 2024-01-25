# 5073 삼각형과 세 변
while True:
  arr = list(map(int, input().split()))
  if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
    break
  arr.sort()
  if arr[0] + arr[1] <= arr[2]:
    print('Invalid')
  elif len(set(arr)) == 1:
    print('Equilateral')
  elif len(set(arr)) == 2:
    print('Isosceles')
  elif len(set(arr)) == 3:
    print('Scalene')