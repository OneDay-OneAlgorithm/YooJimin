# 2447 별찍기
N = int(input())

def draw(n):
  if n == 1: # n이 1인 경우
    return '*' # * 한개
  
  result = []
  stars = draw(n // 3) # 재귀적으로 n -> n // 3 -> ... -> 1

  for star in stars:
    result.append(star * 3) # 별
  for star in stars:
    result.append(star + ' '*(n//3) + star) # 공백
  for star in stars:
    result.append(star * 3)
  return result

ans = draw(N)
print(*ans, sep='\n')