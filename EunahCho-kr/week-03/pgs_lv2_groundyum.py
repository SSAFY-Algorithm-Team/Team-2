# 프로그래머스 Lv2 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 시간 30분 / 시도 2회


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    for i in range(n -1, 0, -1):
        for j in range(m):
            land[i-1][j] += max([land[i][k] for k in range(m) if k != j])

    answer = max(land[0])
    return answer