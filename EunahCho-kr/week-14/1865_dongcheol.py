# 1865 동철이의 일 분배
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc&categoryId=AV5LuHfqDz8DFAXc&categoryType=CODE&problemTitle=1865&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 2h 30m

import sys

sys.stdin = open('1865_input.txt', 'r')


def dfs(i, percent):
    global best, visited

    # 지금까지 곱한 누적 퍼센트가 best보다 작다면, 1보다 적은 값을 곱한다고 커질리가 없음!! 기각
    if percent < best: 
        return
    
    # 종료조건 (N까지 탐색했으면 끝)
    if i == N: 
        best = max(percent, best)
        return
    
    for j in range(N):
        new_percent = percent * percents[i][j]
        # j번째 일을 맡은 사람이 없을 때 탐색 가능
        # 새로 구한 확률이 memo에 기록된 확률보다 클 때만 의미 있음
        if not visited[j] and new_percent > memo[i][j]:
            visited[j] = True  # j번째 일 맡았다! 체크
            memo[i][j] = new_percent  # 이 확률이 최대다! 기록
            dfs(i + 1, percent * percents[i][j] / 100)
            visited[j] = False
            memo[i][j] = percent


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    percents = [list(map(int, input().split())) for _ in range(N)]

    best = 0
    visited = [False] * N  # 해당 일을 맡은 사람이 있는지 체크
    memo = [[-1] * N for _ in range(N)]  # i번째 사람이 j번째 일을 맡을 때 최대 확률 기록용
    dfs(0, 1)

    print(f"#{tc} {best * 100:.6f}")