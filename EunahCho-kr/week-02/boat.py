# programmers 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 시간 : 1h 15m / 시도 : 5

def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boat = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            boat += 1
        elif people[right] <= limit:
            right -= 1
            boat += 1
        elif people[left] <= limit:
            left += 1
            boat += 1

    return boat