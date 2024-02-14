# 20006 랭킹전 대기열
import sys
input = sys.stdin.readline

p, m = map(int, input().rstrip().split()) # p: 플레이어 수, m: 방 정원
room = []

for _ in range(p):
  l, n = input().rstrip().split()
  flag = False # 매칭 가능한 방이 있는지 체크하기 위한 플래그
  for room_list in room:
    # 게임 플레이가 가능한 인원 수 미달, 절대값을 통해 -10 ~ +10 범위 체크
    if len(room_list) < m and abs(int(l) - room_list[0][0]) <= 10:
      room_list.append((int(l), n))
      flag = True # 매칭 가능한 방이 있으므로, True로 변경
      break
  if not flag: # 매칭 가능한 방이 없을 경우
    room.append([(int(l), n)]) # 새 방을 만들고, 입장시킴

for room_list in room:
  print('Started!' if len(room_list) == m else 'Waiting!')
  room_list.sort(key= lambda x: x[-1]) # 닉네임에 맞춰 정렬
  for l, n in room_list:
    print(l, n)