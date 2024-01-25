# 1157 단어 공부

arr = list(map(str, input().lower()))
alpha = [0 for _ in range(26)]

for i in range(len(alpha)):
  alpha[i] = arr.count(chr(97 + i))

candi = list(filter(lambda x:alpha[x] == max(alpha), range(len(alpha))))
print(chr(97 + candi[0]).upper() if len(candi) == 1 else '?')