# programmers 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 시간 : 1h / 시도 : 4

def solution(people, limit):
    people.sort(reverse=True)
    print(people) 
    n = len(people)
    survived = [False] * n
    boat = 0
    while any(survived):
        for i in range(n):
            remain = limit - people[i]
            while remain 
        # for j in range(i + 1, n):
            if people[j] <= remain and not survived[j]:
                survived[j] = True
                # print(survived) #
                remain -= people[j]
        boat += 1

    return boat


""" 거의 반 테케 실패,,;
def solution(people, limit):
    n = len(people)
    survived = [True] + [False] * (n - 1)
    boats = [people[0]]

    for i in range(1, n):
        if not survived[i]:
            for j in range(len(boats)):
                if boats[j] + people[i] <= limit:
                    boats[j] += i
                    survived[i] = True
                    break

        if not survived[i]:
            boats.append(people[i])

    return len(boats)"""


""" test case 16부터 실패
def solution(people, limit):
    people.sort()
    n = len(people)
    survived = [False] * n
    boat = 0
    for i in range(n):
        if not survived[i]:
            survived[i] = True
            remain = limit - people[i]
            for j in range(n - 1, i, -1):
                if people[j] <= remain and not survived[j]:
                    survived[j] = True
                    remain -= people[j]
            boat += 1

    return boat
"""