# 5521. 상원이의 생일파티
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWO3kT6F2oDFAV4&categoryId=AWWO3kT6F2oDFAV4&categoryType=CODE&problemTitle=5521&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 30분 / 2회

import sys

sys.stdin = open('5521_input.txt')


def find_friends(people):
    
    if 1 not in people:
        return 0

    friends = set()
    friends.update(people[1])

    for per in people[1]:
        if per in people:
            friends.update(people[per])

    return len(friends) - 1  # 1(상원)은 초대장 주는 목록에서 빼야됨


T = int(input())
for tc in range(1, T + 1):  
    N, M = map(int, input().split())
    
    people = {}
    for _ in range(M):
        
        a, b = map(int, input().split())
        
        if a not in people:
            people[a] = [b]
        else:
            people[a].append(b)

        if b not in people:
            people[b] = [a]
        else:
            people[b].append(a) # 여기 좀 더 짧게 줄일 수 없나

    # print(people)

    ans = find_friends(people)

    print(f"#{tc} {ans}")
