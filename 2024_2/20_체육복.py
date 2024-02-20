# https://school.programmers.co.kr/learn/courses/30/lessons/42862?itm_content=course14743
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
	
    for i in reserve[:]:
        if i in lost: # reserve에 있는 요소가 lost에도 공통으로 있는 경우 제거
            reserve.remove(i)
            lost.remove(i)
	
    for i in reserve: 
        if i-1 in lost: # 앞번호부터 확인
            lost.remove(i-1)
        elif i+1 in lost: # 뒷번호 확인
            lost.remove(i+1)
    return n-len(lost)