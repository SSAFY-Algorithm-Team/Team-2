# SWEA 7208. 지도 칠하기 (D4)
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWlHcsEqf1YDFASG
# 2h

import sys


sys.stdin = open('7208_input.txt', 'r')


# 인접하고 색이 같은 국가의 색을 바꿔보면서 가장 짧은 거리 찾기 
def find_min(idx, cnt):
    global best

    if cnt >= best:
        return

    if idx == N:
        best = cnt
        return

    for c in range(1, 5):
        for j in range(idx):
            if matrix[idx][j] and color[j] == c:
                break
        else:
            color[idx] = c
            find_min(idx + 1, cnt + (c != country[idx]))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    country = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 인접하고 색이 같은 국가 탐색
    TARGET = set()
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j]:
                if country[i] == country[j]:
                    TARGET.update((i, j))


    if TARGET:
        best = N + 1
        color = [0] * N
        find_min(0, 0)
    else:
        best = 0

    print(f"#{tc} {best}")

