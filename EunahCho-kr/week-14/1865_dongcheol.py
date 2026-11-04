# 1865 동철이의 일 분배
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc&categoryId=AV5LuHfqDz8DFAXc&categoryType=CODE&problemTitle=1865&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 1h

import sys

sys.stdin = open('1865_input.txt', 'r')


def dfs(i, percent):
    global best, visited
    # print(percent)
    # print(visited)

    if percent < best: # 지금까지 곱한 누적 퍼센트가 best보다 작다면, 1보다 적은 값을 곱한다고 커질리가 없음!! 기각
        return

    if i == N:
        best = max(percent, best)
        return
    
    # key = (v for v in visited)
    # if memo.get(key, float('inf')) < best:
    #     return
    # memo[key] = percent

    for j in range(N):
        if not visited[j]:
            visited[j] = i
            dfs(i + 1, percent * percents[i][j] / 100)
            visited[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    percents = [list(map(int, input().split())) for _ in range(N)]
    
    best = 0
    visited = [False] * N
    memo = {}
    dfs(0, 1)

    print(f"#{tc} {best * 100:.6f}")
