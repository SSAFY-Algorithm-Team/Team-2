# 방이 k개 있음
# 한 번에 한 명씩 신청한 순서대로 배정
# 고객은 투숙하기 원하는 번호를 제출
# 원하는 방이 비어있으면 즉시 배정
# 일단 룸을 배열로 만들거나 하면 세상 큰일남


import sys
sys.setrecursionlimit(10**6)  # 재귀가 깊어질 수 있어서 필요

def solution(k, room_number):
    rooms = {}
    ans = []

    def find(room):
        
        # 빈 방이면 배정하고 반환
        if room not in rooms:
            rooms[room] = room + 1
            return room
        
        # 찬 방이면 다음 빈 방을 재귀로 찾고, 경로 압축
        empty_room = find(rooms[room])
        rooms[room] = empty_room 
        return empty_room

    for r in room_number:
        ans.append(find(r))

    return ans